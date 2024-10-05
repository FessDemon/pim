"""Итерационный метод"""

import numpy as np

A = [[-3, 0.5, 0.5], [0.5, -6, 0.5], [0.5, 0.5, -3]]
B = [-56.5, -100, -210]

# точность итераций
EPS = 1e-4

a = np.array(A)  # формируем массив
diag = (1 / np.diag(a)).reshape(-1, 1)
a[np.diag_indices_from(a)] = 0
a = np.hstack((-a, np.array(B).reshape(-1, 1))) * diag
x = a[:, -1].ravel()
x = np.append(x, 1)

tmp = x.copy() + EPS

COUNTER = 0
while abs(x - tmp).sum() > EPS:
    tmp = x.copy()
    x = a.dot(x)
    x = np.append(x, 1)
    COUNTER += 1

print(f"Ответ: {x[:-1].round()}, количество итераций: {COUNTER}")

print(A.dot(x) - B)
