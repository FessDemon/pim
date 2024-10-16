import numpy as np


def is_magic_square(matrix):
    n = len(matrix)

    # Проверка на квадратность
    if any(len(row) != n for row in matrix):
        return False

    # Вычисление магической константы
    magic_constant = sum(matrix[0])

    # Проверка сумм строк
    for row in matrix:
        if sum(row) != magic_constant:
            return False

    # Проверка сумм столбцов
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != magic_constant:
            return False

    # Проверка главной диагонали
    if sum(matrix[i][i] for i in range(n)) != magic_constant:
        return False

    # Проверка побочной диагонали
    if sum(matrix[i][n - 1 - i] for i in range(n)) != magic_constant:
        return False

    return True


# Пример использования
square = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

print(is_magic_square(square))  # Вывод: True
