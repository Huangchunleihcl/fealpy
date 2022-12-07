'''
Title: 2D 抛物方程基于向前Euler格式的有限差分

Author:  梁一茹

Address: 湘潭大学  数学与计算科学学院

'''

import numpy as np
from scipy.sparse import csr_matrix, diags, coo_matrix
import matplotlib.pyplot as plt

from fealpy.mesh import StructureQuadMesh
from fealpy.timeintegratoralg import UniformTimeLine
from fealpy.tools.show import showmultirate, show_error_table


# 准备模型数据
class moudle:
    def __init__(self, T0, T1, nx, ny, NT):
        self.T0 = T0
        self.T1 = T1

        self.nx = nx
        self.ny = ny
        self.NT = NT
        self.domain = domain

    def space_mesh(self):
        mesh = StructureQuadMesh(domain, nx=self.nx, ny=self.ny)
        return mesh

    def time_mesh(self):
        time = UniformTimeLine(self.T0, self.T1, self.NT)
        return time

    def solution(self, p, t):
        x = p[..., 0]
        y = p[..., 1]
        return (x ** 2) * (y ** 2) * (t ** 2)

    def source(self, p, t):
        x = p[..., 0]
        y = p[..., 1]
        return (2 * t * (x ** 2) * (y ** 2)) - (2 * t ** 2 * (x ** 2 + y ** 2))

    def dirichlet(self, p, t):
        return self.solution(p, t=t)

    def is_dirichlet_boundary(self, p):
        eps = 1e-12
        x0, x1, y0, y1 = self.domain
        x = p[..., 0]
        y = p[..., 1]
        flag0 = np.abs(x - x0) < eps
        flag1 = np.abs(x - x1) < eps
        flag2 = np.abs(y - y0) < eps
        flag3 = np.abs(y - y1) < eps
        return flag0 | flag1 | flag2 | flag3


# 向前差分格式
def parabolic_fd2d_forward(pde, mesh, time):
    NT = time.NL - 1
    dt = time.dt
    hx = mesh.hx
    hy = mesh.hy

    n0 = pde.nx + 1
    n1 = pde.ny + 1
    cx = 1 / (hx ** 2)
    cy = 1 / (hy ** 2)

    assert dt <= 1 / (2 * (1 / hx ** 2 + 1 / hy ** 2)), 'dt should be smaller than 1/(2*(1/hx**2+1/hy**2))! Now its value is {}'.format(dt)

    # 组装矩阵
    NN = n0 * n1

    k = np.arange(NN).reshape(n0, n1)

    A = diags([1 - 2 * dt * (cx + cy)], [0], shape=(NN, NN), format='coo')

    val = np.broadcast_to(dt * cy, (NN - n1,))
    I = k[1:, :].flat
    J = k[0:-1, :].flat
    A += coo_matrix((val, (I, J)), shape=(NN, NN), dtype=np.float64)
    A += coo_matrix((val, (J, I)), shape=(NN, NN), dtype=np.float64)

    val = np.broadcast_to(dt * cx, (NN - n0,))
    I = k[:, 1:].flat
    J = k[:, 0:-1].flat
    A += coo_matrix((val, (I, J)), shape=(NN, NN), dtype=np.float64)
    A += coo_matrix((val, (J, I)), shape=(NN, NN), dtype=np.float64)
    A = A.toarray()

    F = np.zeros(NN, dtype=np.float64)

    uh = np.zeros((NT + 1, NN), dtype=np.float64)
    u = np.zeros((NT + 1, NN), dtype=np.float64)

    p = mesh.entity('node')
    uh[0] = pde.solution(p, t=0)

    for i in range(NT):
        nt = time.next_time_level()
        ct = time.current_time_level()

        F[:] = dt * pde.source(p, ct)

        uh[i + 1] = A @ uh[i] + F

        isBdNode = mesh.ds.boundary_node_flag()

        uh[i + 1][isBdNode] = pde.dirichlet(p[isBdNode], nt)
        u[i + 1] = pde.solution(p, nt)
        time.advance()
    return uh, u


if __name__ == '__main__':
    T0 = 0
    T1 = 1

    nx = 10
    ny = 10
    NT = 500
    domain = [0, 1, 0, 1]

    pde = moudle(T0, T1, nx, ny, NT)
    mesh = pde.space_mesh()
    time = pde.time_mesh()

    maxit = 4
    errorType = ['$|| u - u_h||_{C}$', '$|| u - u_h||_{0}$', '$|| u - u_h||_{\ell_2}$']
    errorMatrix = np.zeros((3, maxit), dtype=np.float64)
    NDof = np.zeros(maxit, dtype=np.int_)

    for n in range(maxit):
        uh, u = parabolic_fd2d_forward(pde, mesh, time)

        emax, e0, e1 = mesh.error(mesh.hx, mesh.hy, nx, ny,
                                  u=u[-1], uh=uh[-1])

        errorMatrix[0, n] = emax
        errorMatrix[1, n] = e0
        errorMatrix[2, n] = e1

        NDof[n] = (nx + 1) * (ny + 1)

        if n < maxit - 1:
            nx *= 2
            ny *= 2

            time.uniform_refine()

    show_error_table(NDof, errorType, errorMatrix)
    showmultirate(plt, 0, NDof, errorMatrix, errorType, propsize=10)
    plt.show()