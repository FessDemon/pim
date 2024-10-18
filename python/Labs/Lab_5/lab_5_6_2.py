import numpy as np

m = 4
n = 5
k = 1

a = [[0] * m for i in range(n)]
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            a[i][j] = k
            k += 1
    elif i % 2 == 1:
        for j in range(m - 1, -1, -1):
            a[i][j] = k
            k += 1

for row in a:
    print(" ".join([str(elem) for elem in row]))
