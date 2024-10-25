import numpy as np

A = np.matrix('-3 0.5 0.5; 0.5 -6 0.5; 0.5 0.5 -3')
B = np.matrix('-56.5; -100; -210')
# print(B)
d = np.linalg.det(A)
print(d)
if d == 0:
    print('Определитель матрицы равен 0')
else:
    s_0 = A[:, 0]
    s_1 = A[:, 1]
    s_2 = A[:, 2]

    A_1 = np.column_stack((B, s_1, s_2))
    d_1 = np.linalg.det(A_1)

    A_2 = np.column_stack((s_0, B, s_2))
    d_2 = np.linalg.det(A_2)

    A_3 = np.column_stack((s_0, s_1, B))
    d_3 = np.linalg.det(A_3)

    x_1 = d_1 / d
    x_2 = d_2 / d
    x_3 = d_3 / d

    print(f'Решение системы: {x_1}, {x_2}, {x_3}')

    X = np.array([[x_1], [x_2], [x_3]])
    print(X)

    print(A.dot(X) - B)