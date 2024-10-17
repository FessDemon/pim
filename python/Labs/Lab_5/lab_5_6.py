import numpy as np


def fill_array_method_1(n, m):
    array = np.zeros((n, m), dtype=int)
    num = 1
    for col in range(m):
        if col % 2 == 0:
            for row in range(n):
                array[row, col] = num
                num += 1
        else:
            for row in range(n - 1, -1, -1):
                array[row, col] = num
                num += 1
    return array


def fill_array_method_2(n, m):
    array = np.zeros((n, m), dtype=int)
    num = 1
    for row in range(n):
        if row % 2 == 0:
            for col in range(m):
                array[row, col] = num
                num += 1
        else:
            for col in range(m - 1, -1, -1):
                array[row, col] = num
                num += 1
    return array


def write_to_file(array, filename='python/Labs/Lab_5/task_5_6'):
    np.savetxt(filename, array, fmt='%d')


def main():
    n = int(input("Введите количество строк (n): "))
    m = int(input("Введите количество столбцов (m): "))

    method = int(input("Выберите способ заполнения (1 или 2): "))

    if method == 1:
        filled_array = fill_array_method_1(n, m)
    elif method == 2:
        filled_array = fill_array_method_2(n, m)
    else:
        print("Неверный выбор способа заполнения.")
        return

    write_to_file(filled_array)
    print(f"Массив успешно записан в файл {'python/Labs/Lab_5/task_5_6'}.")


if __name__ == "__main__":
    main()
