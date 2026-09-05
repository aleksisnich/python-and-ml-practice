from scipy.linalg import cho_factor, cho_solve, cho_solve_banded, cholesky_banded
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import time
from mpl_toolkits import mplot3d

nx = 100
ny = 100
xl = -2
xr = 2
yl = -2
yr = 2
N = (ny + 1) * nx
M = nx

lin = np.linspace(xl, xr, nx+1, dtype=np.float64)
hx = lin[1] - lin[0]

lin = np.linspace(yl, yr, ny+1, dtype=np.float64)
hy = lin[1] - lin[0]

A = np.zeros((N, N), dtype=np.float64)
rhs = np.zeros (N, dtype=np.float64)


# задаем функции
def u(x, y):
    # out = 5
    out = x ** 2
    return out


def k1(x, y):
    out = 1
    return out


def k2(x, y):
    out = 1
    return out


def f(x, y):
    # out = 0
    out = 2
    return out


def g1(y):
    out = 5
    return out


def g2(y):
    out = 0
    return out


def g3(x):
    out = 0
    return out


def g4(x):
    out = 0
    return out


def chi2(y):
    out = 0
    return out


def chi3(x):
    out = 0
    return out


def chi4(x):
    out = 0
    return out


def x_i(i):
    return xl + i * hx


def y_i(j):
    return yl + j * hy


def k1_i(i, j):
    return k1(x_i(i), y_i(j))


def k2_i(i, j):
    return k2(x_i(i), y_i(j))


def f_i(i, j):
    return f(x_i(i), y_i(j))


def g1_i(j):
    return g1(y_i(j))


def g2_i(j):
    return g2(y_i(j))


def g3_i(i):
    return g3(x_i(i))


def g4_i(i):
    return g4(x_i(i))


def chi2_i(j):
    return chi2(y_i(j))


def chi3_i(i):
    return chi3(y_i(i))


def chi4_i(i):
    return chi4(y_i(i))


for i in range(1, nx + 1):
    for j in range(0, ny+1):
        m = j*M + i - 1
        if i == nx and j == 0:
            A[m][m] = (hy/2) * chi2_i(0) +\
                      hy * k1_i(nx-1/2, 0) / (2*hx) +\
                      hx * k2_i(nx, 1/2) / (2*hy) +\
                      (hx/2) * chi3_i(nx)

            A[m][m+M] = - hx * k2_i(nx, 1/2) / (2*hy)

            A[m][m-1] = - hy * k1_i(nx-1/2, 0) / (2*hx)

            rhs[m] = (hx/2) * (hy/2) * f_i(nx, 0) +\
                     g2_i(0) * (hy/2) +\
                     g3_i(nx) * (hx/2)
        elif i == nx and j == ny:
            A[m][m] = (hy/2) * chi2_i(ny) +\
                      hy * k1_i(nx-1/2, ny) / (2*hx) +\
                      (hx/2) * chi4_i(nx) +\
                      hx * k2_i(nx, ny-1/2) / (2*hy)

            A[m][m-M] = - hx * k2_i(nx, ny-1/2) / (2*hy)

            A[m][m-1] = - hy * k1_i(nx-1/2, ny) / (2*hx)

            rhs[m] = (hx/2) * (hy/2) * f_i(nx, ny) +\
                     g2_i(ny) * (hy/2) +\
                     g4_i(nx) * (hx/2)

        elif i == 1 and j == 0:
            A[m][m] = hy * k1_i(3/2, 0) / (2*hx) +\
                      hy * k1_i(1/2, 0) / (2*hx) +\
                      hx * k2_i(1, 1/2) / hy +\
                      hx * chi3_i(1)

            A[m][m+M] = - hx * k2_i(1, 1/2) / hy

            A[m][m+1] = - hy * k1_i(3/2, 0) / (2*hx)

            rhs[m] = hx*hy/2 * f_i(1, 0) + g3_i(1) * hx + hy/(2*hx) * k1_i(1/2, 0) * g1_i(0)

        elif i == 1 and j == ny:
            A[m][m] = hy * k1_i(3/2, ny) / (2*hx) +\
                      hy * k1_i(1/2, ny) / (2*hx) +\
                      hx * chi4_i(1) +\
                      hx * k2_i(1, ny-1/2) / hy

            A[m][m-M] = - hx * k2_i(1, ny-1/2) / hy

            A[m][m+1] = - hy * k1_i(3/2, ny) / (2*hx)

            rhs[m] = hx*hy/2 * f_i(1, ny) + g4_i(1) * hx + hy/(2*hx) * k1_i(1/2, ny) * g1_i(ny)

        elif i == nx and 1 <= j <= ny-1:

            A[m][m] = hy * chi2(j) +\
                      hy * k1_i(nx-1/2, j) / hx +\
                      hx * k2_i(nx, j+1/2) / (2*hy) +\
                      hx * k2_i(nx, j-1/2) / (2*hy)

            A[m][m-1] = - hy * k1_i(nx-1/2, j) / hx

            A[m][m+M] = - hx * k2_i(nx, j+1/2) / (2*hy)

            A[m][m-M] = - hx * k2_i(nx, j-1/2) / (2*hy)

            rhs[m] = hx * hy / 2 * f_i(nx, j) + hy * g2_i(j)

        elif j == 0 and 2 <= i <= nx-1:

            A[m][m] = hy * k1_i(i+1/2, 0) / (2*hx) +\
                      hy * k1_i(i-1/2, 0) / (2*hx) +\
                      hx * k2_i(i, 1/2) / hy +\
                      hx * chi3_i(i)

            A[m][m-1] = -hy * k1_i(i-1/2, 0) / (2*hx)

            A[m][m+1] = -hy * k1_i(i+1/2, 0) / (2*hx)

            A[m][m+M] = -hx * k2_i(i, 1/2) / hy

            rhs[m] = hx*hy/2 * f_i(i, 0) + g3_i(i) * hx

        elif j == ny and 2 <= i <= nx-1:

            A[m][m] = hy * k1_i(i+1/2, ny) / (2*hx) +\
                      hy * k1_i(i-1/2, ny) / (2*hx) +\
                      hx * chi4_i(i) +\
                      hx * k2_i(i, ny-1/2) / hy

            A[m][m-1] = - hy * k1_i(i-1/2, ny) / (2*hx)

            A[m][m+1] = - hy * k1_i(i+1/2, ny) / (2*hx)

            A[m][m-M] = - hx * k2_i(i, ny-1/2) / hy

            rhs[m] = hx*hy/2 * f_i(i, ny) + g4_i(i) * hx

        elif i == 1 and 1 <= j <= ny-1:
            A[m][m] = hy * k1_i(3/2, j) / hx +\
                      hy * k1_i(1/2, j) / hx +\
                      hx * k2_i(1, j+1/2) / hy +\
                      hx * k2_i(1, j-1/2) / hy

            A[m][m-M] = -hx * k2_i(1, j-1/2) / hy

            A[m][m+M] = -hx * k2_i(1, j+1/2) / hy

            A[m][m+1] = -hy * k1_i(3/2, j) / hx

            rhs[m] = hx * hy * f_i(1, j) + g1_i(j) * hy/hx * k1_i(1/2, j)

        else:
            A[m][m] = hy * k1_i(i+1/2, j) / hx +\
                      hy * k1_i(i-1/2, j) / hx +\
                      hx * k2_i(i, j+1/2) / hy +\
                      hx * k2_i(i, j-1/2) / hy

            A[m][m-M] = -hx * k2_i(i, j-1/2) / hy

            A[m][m+M] = -hx * k2_i(i, j+1/2) / hy

            A[m][m-1] = -hy * k1_i(i-1/2, j) / hx

            A[m][m+1] = -hy * k1_i(i+1/2, j) / hx

            rhs[m] = hx * hy * f_i(i, j)


print('Собрал матрицу системы')

# cond = np.linalg.cond(A, p=None)  # вычисление числа обусловленности, p=None - нормой является корень из суммы квадратов
print('Посчитал число обусловленности')

print('hx :', hx)
print('hy :', hy)
print(A)
# print(rhs)
# print('Condition number :', cond)

Ab = np.array([])
for i in range(M, -1, -1):
    Ab = np.append(Ab, np.zeros(i))
    Ab = np.append(Ab, np.diag(A, i))
Ab = Ab.reshape(M+1, N)
print(Ab)

Ab_chol = cholesky_banded(Ab, overwrite_ab=True, lower=False, check_finite=True)
print('Сделал разложение')

Ab_chol_sol = cho_solve_banded((Ab_chol, False), rhs, overwrite_b=True, check_finite=True)
print('Решил систему')

print(Ab_chol_sol)
x = Ab_chol_sol.reshape(ny+1, nx)
# print('Solution', x)
print('Peak :', np.max(x))

# plt.imshow(x)
# plt.show()
fig = plt.figure()
ax = plt.axes(projection='3d')
X, Y = np.meshgrid(np.linspace(xl, xr, nx+1)[1:], np.linspace(yl, yr, ny+1))
ax.plot_surface(X, Y, x, rstride=1, cstride=1, cmap='plasma', edgecolor='none')
# ax.plot_wireframe(X, Y, u(X, Y), color='black')
# print('Error :')
# print(x-u(X, Y))
print('Error norm :', np.max(np.abs(x-u(X, Y))))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('U')
ax.set_title('Numeric solution')


fig.tight_layout()
plt.show()