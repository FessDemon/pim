import numpy as np

A = np.matrix('-3 0.5 0.5; 0.5 -6 0.5; 0.5 0.5 -3')
B = np.matrix('-56.5; -100; -210')
X = np.linalg.solve(A, B)
for t, x in zip(X, ['x1=', 'x2=', 'x3=']):
    print(x ,t)

print(X)
print(A.dot(X) - B)

