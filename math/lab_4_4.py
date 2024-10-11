# Метод LU-разложения
import numpy as np
from scipy.linalg import lu, solve_triangular

A = np.loadtxt("math/matrix_A.txt")
B = np.loadtxt("math/matrix_B.txt")


def solve_LU(A, B):

    p, L, U = lu(A)  # Разложение матрицы А методом LU-разложения
    y = solve_triangular(
        L, B, lower=True, check_finite=False
    )  # Нахождение y, как решения уравнения L*y=B
    x = solve_triangular(
        U, y, check_finite=False
    )  # Нахождение x, как решения уравнения U*x=y
    return x


print("\nРешение методом LU-разложения: ")
x = solve_LU(A, B)
print("x = ", x)
# Проверка
# Вычисление невязки
print(A.dot(x) - B)
