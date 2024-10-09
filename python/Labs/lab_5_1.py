import random
import numpy as np


while True:
    try:
        n = int(input("Введите положительное целое число: "))
        if n > 0:
            break
        else:
            print("Число должно быть больше 0! Попробуйте еще раз.")
    except ValueError:
        print("Некорректный ввод! Попробуйте еще раз.")

arr_f = np.array([random.uniform(-10, 10) for x in range(n)])
print(f"Массив из {n} случайных вещественных чисел из диапазона [-10; 10]")
print(arr_f)

min_arr_f = min(arr_f)
print(f"min = {min_arr_f}")

max_arr_f = max(arr_f)
print(f"max = {max_arr_f}")

y = random.uniform(min_arr_f, max_arr_f)
print(f"y = {y}")

p = 1
s = 0
for i in range(n):
    if abs(arr_f[i]) > abs(y):
        p *= arr_f[i]
    else:
        s += arr_f[i]
print(f"p = {p}, s = {s}")
