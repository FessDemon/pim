import numpy as np


def fill_array_first_way(n, m):
    # Создаем пустой массив размером n x m
    array = np.zeros((n, m), dtype=int)

    for i in range(1, n * m + 1):
        row = i // m
        col = i % m
        array[row][col] = i

    return array


def fill_array_second_way(n, m):
    # Создаем пустой массив размером n x m
    array = np.zeros((n, m), dtype=int)

    for i in range(m*n):
        if i == 0 or i >= (m+1)*n/2:
            j = int(i / n)
            k = i % n
            array[j][k] = i + 1
        else:
            j = int(i / n)
            k = n - 1 - (i % n)
            array[j][k] = i + 1

    return array


# Запрашиваем размерность массива и способ заполнения у пользователя
n = int(input("Введите размерность n: "))
m = int(input("Введите размерность m: "))
mode = int(input("Введите номер способа (1 или 2): "))

if mode == 1:
    filled_array = fill_array_first_way(n, m)
elif mode == 2:
    filled_array = fill_array_second_way(n, m)
else:
    print("Неверный номер способа")
    exit()

# Сохраняем результат в файл
np.savetxt('python/Labs/Lab_5/task_5_6/result.txt', filled_array, fmt='%d')
print("Заполненный массив сохранен в файл result.txt")
