import numpy as np


def method_1(rows, cols):
    matrix = np.zeros((rows, cols), dtype=int)

    # Список чисел для матрицы
    numbers = list(range(1, rows * cols + 1))

    # Индекс для доступа к элементам списка numbers
    index = 0

    # Проходим по всем возможным диагоналям матрицы (их количество = rows + cols - 1)
    for diagonal in range(rows + cols - 1):
        if diagonal % 2 == 0:  # Для четных диагоналей (0, 2, 4,...)
            for i in range(rows):  # Проходим по всем строкам
                j = diagonal - i  # Вычисляем соответствующий столбец
                # Проверяем, что индекс столбца j находится в пределах матрицы
                if 0 <= j < cols:
                    matrix[i, j] = numbers[
                        index
                    ]  # Записываем число из списка в матрицу
                    index += 1  # Увеличиваем индекс для доступа к следующему числу
        else:  # Для нечетных диагоналей (1, 3, 5,...)
            for i in range(rows - 1, -1, -1):  # Проходим по строкам в обратном порядке
                j = diagonal - i  # Вычисляем соответствующий столбец
                # Проверяем, что индекс столбца j находится в пределах матрицы
                if 0 <= j < cols:
                    matrix[i, j] = numbers[
                        index
                    ]  # Записываем число из списка в матрицу
                    index += 1  # Увеличиваем индекс для доступа к следующему числу
    return matrix


def method_2(rows, cols):
    matrix = np.zeros((rows, cols), dtype=int)

    # Инициализируем границы для спирального движения
    top, bottom = 0, rows - 1  # Верхняя и нижняя границы
    left, right = 0, cols - 1  # Левая и правая границы

    # Стартовое число
    num = 1

    # Продолжаем, пока верхняя граница меньше или равна нижней, а левая меньше или равна правой
    while top <= bottom and left <= right:
        # Заполняем верхнюю строку (движемся слева направо)
        for i in range(left, right + 1):
            matrix[top, i] = num  # Записываем число в текущую ячейку
            num += 1  # Увеличиваем число
        top += 1  # Смещаем верхнюю границу вниз

        # Заполняем правый столбец (движемся сверху вниз)
        for i in range(top, bottom + 1):
            matrix[i, right] = num  # Записываем число в текущую ячейку
            num += 1  # Увеличиваем число
        right -= 1  # Смещаем правую границу влево

        # Заполняем нижнюю строку (движемся справа налево, если остались строки для заполнения)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom, i] = num  # Записываем число в текущую ячейку
                num += 1  # Увеличиваем число
            bottom -= 1  # Смещаем нижнюю границу вверх

        # Заполняем левый столбец (движемся снизу вверх, если остались столбцы для заполнения)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i, left] = num  # Записываем число в текущую ячейку
                num += 1  # Увеличиваем число
            left += 1  # Смещаем левую границу вправо

    return matrix


def print_matrix(matrix, title):
    print(title)
    for row in matrix:
        print(" ".join(f"{x:3}" for x in row))
    print()


def main():
    rows, cols = 5, 5

    matrix1 = method_1(rows, cols)
    matrix2 = method_2(rows, cols)

    print_matrix(matrix1, "Способ 1:")
    print_matrix(matrix2, "Способ 2:")


if __name__ == "__main__":
    main()
