"""Итерационный метод вариант № 2"""

A = [[-3, 0.5, 0.5], [0.5, -6, 0.5], [0.5, 0.5, -3]]
B = [-56.5, -100, -210]

# точность итераций
EPS = 1e-4
x = []
N = len(A)
for j in range(N):
    k = A[j][j]
    for i in range(N):
        A[j][i] /= -k
    A[j][j] = 0
    B[j] /= k

# r - счетчик итераций
R = 0
x = B.copy()
tmp = sum(x) + 2 * EPS
while abs(sum(x) - tmp) > EPS:
    tmp = sum(x)
    t = [0] * N
    for i in range(N):
        t[i] = sum(x[j] * A[i][j] for j in range(N)) + B[i]
    R += 1
    x = t.copy()

print(*(round(elem) for elem in x))
print(R)
