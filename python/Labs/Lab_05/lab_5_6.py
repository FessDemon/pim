import numpy as np


def method_1(rows, cols):
    matrix = np.zeros((rows, cols), dtype=int)

    # Список чисел для матрицы
    numbers = list(range(1, rows * cols + 1))

    # Индекс для доступа к элементам списка numbers
    index = 0

    # Проходим по всем возможным диагоналям матрицы
    # (их количество = rows + cols - 1)
    for diagonal in range(rows + cols - 1):
        if diagonal % 2 == 0:  # Для четных диагоналей (0, 2, 4,...)
            for i in range(rows):  # Проходим по всем строкам
                j = diagonal - i  # Вычисляем соответствующий столбец
                # Проверяем, что индекс столбца j находится в пределах матрицы
                if 0 <= j < cols:
                    # Записываем число из списка в матрицу
                    matrix[i, j] = numbers[index]
                    index += 1  # Увеличиваем индекс для доступа к следующему числу
        else:  # Для нечетных диагоналей (1, 3, 5,...)
            for i in range(rows - 1, -1, -1):  # Проходим по строкам в обратном порядке
                j = diagonal - i  # Вычисляем соответствующий столбец
                # Проверяем, что индекс столбца j находится в пределах матрицы
                if 0 <= j < cols:
                    # Записываем число из списка в матрицу
                    matrix[i, j] = numbers[index]
                    index += 1  # Увеличиваем индекс для доступа к следующему числу
    return matrix


def method_2(rows, cols):
    matrix = np.zeros((rows, cols), dtype=int)

    # Инициализируем границы для спирального движения
    top, bottom = 0, rows - 1  # Верхняя и нижняя границы
    left, right = 0, cols - 1  # Левая и правая границы

    # Стартовое число
    num = 1

    while top <= bottom and left <= right:
        # Заполняем верхнюю строку (слева направо)
        matrix[top, left : right + 1] = np.arange(num, num + (right - left + 1))
        num += right - left + 1
        top += 1

        # Заполняем правый столбец (сверху вниз)
        if top <= bottom:
            matrix[top : bottom + 1, right] = np.arange(num, num + (bottom - top + 1))
            num += bottom - top + 1
            right -= 1

        # Заполняем нижнюю строку (справа налево)
        if left <= right:
            matrix[bottom, left : right + 1] = np.arange(num, num + (right - left + 1))[
                ::-1
            ]
            num += right - left + 1
            bottom -= 1

        # Заполняем левый столбец (снизу вверх)
        if top <= bottom:
            matrix[top : bottom + 1, left] = np.arange(num, num + (bottom - top + 1))[
                ::-1
            ]
            num += bottom - top + 1
            left += 1

    return matrix


def print_matrix(matrix, title):
    print(title)
    for row in matrix:
        print(" ".join(f"{x:3}" for x in row))
    print()


# Запрашиваем целое положительно число - количество столбцов или количество строк
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Ошибка: введите положительное целое число.")
        except ValueError:
            print("Ошибка: введите целое число.")


# Запрашиваем выбор метода заполнения матрицы (1 или 2).
def get_method_choice():
    while True:
        choice = input("Выберите метод заполнения матрицы (1 или 2): ")
        if choice in ["1", "2"]:
            return int(choice)
        else:
            print("Ошибка: введите 1 или 2.")


def main():
    rows = get_positive_int("Введите количество строк (положительное целое число): ")
    cols = get_positive_int("Введите количество столбцов (положительное целое число): ")
    method = get_method_choice()
    if method == 1:
        matrix = method_1(rows, cols)
        print_matrix(matrix, "Способ 1:")
    elif method == 2:
        matrix = method_2(rows, cols)
        print_matrix(matrix, "Способ 2:")


if __name__ == "__main__":
    main()
