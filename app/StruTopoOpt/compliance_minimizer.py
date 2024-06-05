import jax
import jax.numpy as jnp
from jax import jit, value_and_grad
from utilfuncs import Mesher
 
def test_projectionFilter(rho, beta, c0, isOn):
    if isOn:
        v1 = jnp.tanh(c0 * beta)
        nm = v1 + jnp.tanh(beta * (rho - c0))
        dnm = v1 + jnp.tanh(beta * (1. - c0))
        return nm / dnm
    else:
        return rho

class ComplianceMinimizer:
    def __init__(self, 
                 mesh = None, 
                 bc = None, 
                 material = None, 
                 globalvolCons = None, 
                 projection = None):
        
        # 默认网格参数
        if mesh is None:
            nelx, nely = 60, 30
            elemSize = jnp.array([1., 1.])
            mesh = {'nelx': nelx, 'nely': nely, 'elemSize': elemSize,
                    'ndof': 2 * (nelx + 1) * (nely + 1), 'numElems': nelx * nely}
        else:
            nelx, nely = mesh['nelx'], mesh['nely']
        
        # 默认材料参数
        if material is None:
            material = {'Emax': 1., 'Emin': 1e-3, 'nu': 0.3, 'penal': 3.}
        
        # 默认全局体积约束
        if globalvolCons is None:
            globalvolCons = {'isOn': True, 'vf': 0.5}
        
        # 默认投影参数
        if projection is None:
            projection = {'isOn': True, 'beta': 4, 'c0': 0.5}
        
        # 默认边界条件和载荷
        if bc is None:
            example = 1
            if example == 1:
                force = jnp.zeros((mesh['ndof'], 1))
                dofs = jnp.arange(mesh['ndof'])
                fixed = dofs[0:2 * (nely + 1):1]
                free = jnp.setdiff1d(jnp.arange(mesh['ndof']), fixed)
                # JAX 数组是不可变的，不能直接进行赋值操作。需要使用 JAX 提供的 .at[].set() 方法来进行修改
                force = force.at[2 * (nelx + 1) * (nely + 1) - 2 * nely + 1, 0].set(-1)
                symXAxis = False
                symYAxis = False
            elif example == 2:
                force = jnp.zeros((mesh['ndof'], 1))
                dofs = jnp.arange(mesh['ndof'])
                fixed = dofs[0:2 * (nely + 1):1]
                free = jnp.setdiff1d(jnp.arange(mesh['ndof']), fixed)
                # JAX 数组是不可变的，不能直接进行赋值操作。需要使用 JAX 提供的 .at[].set() 方法来进行修改
                force = force.at[2 * (nelx + 1) * (nely + 1) - (nely + 1), 0].set(-1)
                symXAxis = True
                symYAxis = False
            else:
                force = jnp.zeros((mesh['ndof'], 1))
                fixed = jnp.array([])
                free = jnp.array([])
                symXAxis = False
                symYAxis = False

            bc = {'force': force, 'fixed': fixed, 'free': free,
                  'symXAxis': symXAxis, 'symYAxis': symYAxis}

        self.mesh = mesh
        self.material = material
        self.bc = bc
        
        # 初始化 Mesher 类并获取初始刚度矩阵
        M = Mesher()
        self.edofMat, self.idx = M.getMeshStructure(mesh)
        self.K0 = M.getK0(self.material)

        # 设置全局体积约束
        self.globalVolumeConstraint = globalvolCons
        
        # 自动微分计算柔顺度和约束
        self.objectiveHandle = jit(value_and_grad(self.computeCompliance))
        self.consHandle = self.computeConstraints
        self.numConstraints = 1
        
        # 设置投影参数
        self.projection = projection

    def computeCompliance(self, rho):

        @jit
        # 投影滤波器
        def projectionFilter(rho):
            if(self.projection['isOn']):
                v1 = jnp.tanh(self.projection['c0'] * self.projection['beta'])
                nm = v1 + jnp.tanh(self.projection['beta'] * (rho - self.projection['c0']))
                dnm = v1 + jnp.tanh(self.projection['beta'] * (1. - self.projection['c0']))
                return nm/dnm
            else:
                return rho

        @jit
        # SIMP 材料插值模型
        def materialModel(rho):
            E = self.material['Emin'] + \
                (self.material['Emax'] - self.material['Emin']) * \
                (rho + 0.01) ** self.material['penal']
            return E
        
        @jit
        # 组装全局刚度矩阵
        def assembleK(E):
            K_asm = jnp.zeros((self.mesh['ndof'], self.mesh['ndof']))
            K_elem = (self.K0.flatten()[jnp.newaxis]).T

            K_elem = (K_elem*E).T.flatten()
            K_asm = K_asm.at[(self.idx)].add(K_elem)
            return K_asm
        
        @jit
        # 直接法求解线性方程组
        def solveKuf(K): 
            u_free = jax.scipy.linalg.solve(K[self.bc['free'],:][:,self.bc['free']], \
                                        self.bc['force'][self.bc['free']], check_finite=False)
            u = jnp.zeros((self.mesh['ndof']))
            u = u.at[self.bc['free']].set(u_free.reshape(-1))
            return u
        
        rho = projectionFilter(rho)
        E = materialModel(rho)
        K = assembleK(E)
        u = solveKuf(K)
        J = jnp.dot(self.bc['force'].T, u)[0]

        return J

    def computeConstraints(self, rho, epoch):
        # 将具体实现填充在这里
        pass

