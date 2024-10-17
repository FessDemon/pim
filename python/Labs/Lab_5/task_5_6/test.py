import numpy as np

n = 4
m = 4
k = 1
# Создаем пустую матрицу размером n x m
matrix = np.zeros((n, m))

for i in range(0, n+1):
    for j in range(0, m+1):
        matrix[i][j] += i

print(matrix)
