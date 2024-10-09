import numpy as np
import random

while True:
    try:
        n = int(input("Введите положительное целое число: "))
        if n > 0:
            break
        else:
            print("Число должно быть больше 0! Попробуйте еще раз.")
    except ValueError:
        print("Некорректный ввод! Попробуйте еще раз.")

arr_f = np.array([random.randint(-5, 5) for x in range(n)])
print(f"Mассив из {n} случайных чисел из диапазона [-10; 10]")
print(arr_f)

arr_f1 = []
for i in range(1, n):
    if arr_f[i - 1] == 0:
        arr_f1.append(arr_f[i])
if arr_f1 != []:
    print(max(arr_f1))
else:
    print("no")
