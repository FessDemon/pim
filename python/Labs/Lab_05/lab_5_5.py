import numpy as np


def is_magic_square(matrix):
    # Преобразуем список в массив NumPy
    arr = np.array(matrix)

    # Проверка на квадратность
    n, m = arr.shape
    if n != m:
        return False

    # Вычисление магической константы
    magic_constant = np.sum(arr[0])

    # Проверка сумм строк
    if not np.all(np.sum(arr, axis=1) == magic_constant):
        return False

    # Проверка сумм столбцов
    if not np.all(np.sum(arr, axis=0) == magic_constant):
        return False

    # Проверка главной диагонали
    if np.sum(np.diag(arr)) != magic_constant:
        return False

    # Проверка побочной диагонали
    if np.sum(np.diag(np.fliplr(arr))) != magic_constant:
        return False

    return True


square = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

is_magic_square(square)

if is_magic_square(square) == True:
    print("Массив является магическим квадратом")
else:
    print("Массив не является магическим квадратом")
