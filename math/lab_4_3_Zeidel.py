"""Метод Зейделя"""

import numpy as np

A = [[-3, 0.5, 0.5], [0.5, -6, 0.5], [0.5, 0.5, -3]]
B = [-56.5, -100, -210]

EPS = 0.0001


def zeidel(A, B, EPS):
    n = len(A)
    x = np.zeros(n)  # zero vector

    converge = False
    while not converge:
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (B[i] - s1 - s2) / A[i][i]

        converge = np.linalg.norm(x_new - x) <= EPS
        x = x_new
    print(x)


zeidel(A, B, EPS)
