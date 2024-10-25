# not ready
import random

ar = [random.randint(-100, 10) for x in range(10)]
# ar = [-1,-2,3,6,5,1,7,8]
# ar=[1,2,3,4,5,-1,-2,-3]
# ar = [-1,-2,3,6,5,1,-7,8]
# ar = [1,1,1,1,1]
# ar = [-1,-1,-1,-1,-1]
print(ar)
ar1 = []

f = True

i_p = 0
while ar[i_p] <= 0 and i_p < len(ar) - 1:
    i_p += 1
# print(i_p)

i_o = len(ar) - 1
while ar[i_o] >= 0 and i_o > 0:
    i_o -= 1
# print(i_o)

# print('первый положительный',i_p,' последний отрицательный', i_o)

# print(abs(i_p - i_o))

# если искомые элементы соседние, или в массиве только положительные
# или только отрицательные числа, то переставлять нечего, f=false
if (i_p - i_o == 1) or (i_o == 0) or (i_p == len(ar) - 1):
    f = False

# print(f)

if not f:
    print("переставлять нечего")
else:
    if i_p < i_o:
        ar1 = ar[: i_p + 1] + sorted(ar[i_p + 1 : i_o]) + ar[i_o:]
    else:
        if i_p > i_o:
            ar1 = ar[:i_p] + sorted(ar[i_o + 1 : i_p - 1] + ar[i_o:])
    print(ar1)
