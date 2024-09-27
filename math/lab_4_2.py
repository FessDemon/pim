import numpy as np

A = np.loadtxt('math/matrixA1.txt')
B = np.loadtxt('math/matrixB1.txt')
matrix = np.loadtxt('math/matrix1.txt')
print(A)
print(B)
print(matrix)

print(f'Решение СЛУ: {np.linalg.solve(A, B)}')
