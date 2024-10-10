import numpy as np


def is_magic_square(matrix):
    # Проверка, что матрица квадратная
    if not matrix or len(matrix) != len(matrix[0]):
        return False

    n = len(matrix)
    # Эталонная сумма (сумма первой строки)
    magic_sum = sum(matrix[0])

    # Проверка сумм строк
    for row in matrix:
        if sum(row) != magic_sum:
            return False

    # Проверка сумм столбцов
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != magic_sum:
            return False

    # Проверка суммы главной диагонали
    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False

    # Проверка суммы побочной диагонали
    if sum(matrix[i][n - 1 - i] for i in range(n)) != magic_sum:
        return False

    return True


# Пример использования
matrix = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

if is_magic_square(matrix):
    print("Массив является магическим квадратом.")
else:
    print("Массив не является магическим квадратом.")
