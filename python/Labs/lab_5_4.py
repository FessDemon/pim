import os
import numpy as np


def read_matrix_from_file(filename):
    try:
        with open(filename, "r") as file:
            matrix = []
            for line in file:
                # Преобразуем строку в список чисел
                row = list(map(int, line.split()))
                if len(row) != 10:
                    raise ValueError("Каждая строка должна содержать 10 элементов.")
                matrix.append(row)
            if len(matrix) != 10:
                raise ValueError("Матрица должна содержать 10 строк.")
            return matrix
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None


def is_local_minimum(matrix, i, j):
    current_value = matrix[i][j]
    neighbors = [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]

    for x, y in neighbors:
        if 0 <= x < 10 and 0 <= y < 10:  # Проверка границ матрицы
            if matrix[x][y] <= current_value:
                return False
    return True


def count_local_minima(matrix):
    count = 0
    for i in range(10):
        for j in range(10):
            if is_local_minimum(matrix, i, j):
                count += 1
    return count


def main():
    matrix = read_matrix_from_file("python/Labs/task_5_4/input.txt")
    if matrix is not None:
        local_minima_count = count_local_minima(matrix)
        print(f"Количество локальных минимумов: {local_minima_count}")
        matrix = np.array(matrix)
        print(matrix)


if __name__ == "__main__":
    main()
