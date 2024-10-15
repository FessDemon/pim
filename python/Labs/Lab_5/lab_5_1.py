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

array = np.random.uniform(-10, 10, n)
print("Сформированный массив:", array)

min_elem = np.min(array)
max_elem = np.max(array)

y = random.uniform(min_elem, max_elem)
print("Случайное число y:", y)

mult = np.prod(np.where(np.abs(array) > np.abs(y), array, 1))
print(f"Произведение элементов массива, модуль которых больше |y| = {mult}")

summa = np.sum(np.where(np.abs(array) <= np.abs(y), array, 0))
print(f"Сумма модулей остальных элементов = {summa}")
