'''
Title: 一维波动方程基于蛙跳格式的有限差分

Author:  梁一茹

Address: 湘潭大学  数学与计算科学学院

'''

import numpy as np
from scipy.sparse import csr_matrix, diags

import matplotlib.pyplot as plt

from fealpy.mesh import StructureIntervalMesh
from fealpy.timeintegratoralg import UniformTimeLine
from fealpy.tools.show import showmultirate, show_error_table

# 准备模型数据
class moudle:
    def __init__(self, L, R, T0, T1, a, NS, NT):
        self.L = L
        self.R = R

        self.T0 = T0
        self.T1 = T1

        self.a = a

        self.NS = NS
        self.NT = NT

    def space_mesh(self):
        mesh = StructureIntervalMesh([self.L, self.R], self.NS)
        return mesh

    def time_mesh(self):
        time = UniformTimeLine(self.T0, self.T1, self.NT)
        return time

    def solution(self, x, t):
        val = (x ** 2) * (t ** 2)
        return val

    def source(self, x, t):
        return (2 * t * x ** 2) + (2 * x * t ** 2)

    def left_solution(self, t):
        return self.solution(x=self.L, t=t)

    def right_solution(self, t):
        return self.solution(x=self.R, t=t)

# 蛙跳格式
def wave_fd1d_leapfrog(pde, mesh, time):
    NS = mesh.NC
    NT = time.NL - 1
    dt = time.dt
    h = mesh.hx

    r = pde.a * dt / h
    x = mesh.entity('node')
    assert np.abs(r) <= 1, 'error, beacuse r={}'.format(r)

    # 组装矩阵
    d0 = np.zeros(NS - 1, dtype=np.float64)

    d1 = np.ones(NS - 2, dtype=np.float64)
    d1[:] = -r

    d2 = np.ones(NS - 2, dtype=np.float64)
    d2[:] = r

    A = diags([d0, d1, d2], [0, 1, -1], shape=(NS - 1, NS - 1), format='csr')

    F = np.zeros(NS - 1, dtype=np.float64)

    uh = np.zeros((NT + 1, NS + 1), dtype=np.float64)

    uh[0] = pde.solution(x, t=0)
    uh[1] = pde.solution(x, t=dt)

    for i in range(NT):
        nt = time.next_time_level()
        ct = time.current_time_level()

        F[:] = 2 * dt * pde.source(x[1:-1], ct)
        F[0] += r * uh[i, 0]
        F[-1] -= r * uh[i, -1]

        uh[i + 1, 0] = pde.left_solution(nt)
        uh[i + 1, -1] = pde.right_solution(nt)

        uh[i+1, 1:-1] = uh[i-1, 1:-1] + A @ uh[i, 1:-1] + F
        time.advance()
    return uh


if __name__ == '__main__':
    L = 0
    R = 1

    T0 = 0
    T1 = 1

    a = 1

    NS = 20
    NT = 100

    pde = moudle(L, R, T0, T1, a, NS, NT)
    mesh = pde.space_mesh()
    time = pde.time_mesh()

    maxit = 4
    errorType = ['$|| u - u_h||_{C}$', '$|| u - u_h||_{0}$', '$|| u - u_h||_{\ell_2}$']
    errorMatrix = np.zeros((3, maxit), dtype=np.float64)
    NDof = np.zeros(maxit, dtype=np.int_)

    for n in range(maxit):
        uh = parabolic_fd1d_leapfrog(pde, mesh, time)

        emax, e0, e1 = mesh.error(h=mesh.hx,
                                  u=lambda x: pde.solution(x, t=T1),
                                  uh=uh[-1, :])

        errorMatrix[0, n] = emax
        errorMatrix[1, n] = e0
        errorMatrix[2, n] = e1

        NDof[n] = mesh.NN

        if n < maxit - 1:
            mesh.uniform_refine()
            time.uniform_refine()

    show_error_table(NDof, errorType, errorMatrix)
    showmultirate(plt, 0, NDof, errorMatrix, errorType, propsize=10)
    plt.show()