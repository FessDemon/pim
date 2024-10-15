import numpy as np
import random

while True:
    try:
        n = int(
            input("Введите положительное целое число для определения длины массива: ")
        )
        if n > 0:
            break
        else:
            print("Число должно быть больше 0! Попробуйте еще раз.")
    except ValueError:
        print("Некорректный ввод! Попробуйте еще раз.")

print(
    "Введи два числа через пробел - диапазон элементов массива [a, b]",
)
d = input().split()
x = np.random.randint(int(d[0]), int(d[1]) + 1, (n,))
print("x = ", x)
# Нахождение максимального значения элементов массива, перед которыми стоит нулевой
zero = x == 0
maximum = np.max(x[1:][zero[:-1]])
print("максимальный элемент массива, перед которым стоит нулевой = ", maximum)
