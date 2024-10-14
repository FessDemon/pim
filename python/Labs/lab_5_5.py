import numpy as np


def mag_matrix(a):
    f = True
    # массив сумм элементов каждого столбца
    sum_col = a.sum(axis=0)
    # проверка, что все полученные суммы одинаковы
    if np.all(sum_col == sum_col[0]):
        # массив сумм элементов каждой строки
        sum_row = a.sum(axis=1)
        # проверка, что массив сумм по строкам совпадает с массивом сумм по столбцам
        if np.array_equal(sum_col, sum_row):
            # сумма элементов на главной диагонали
            sum_gd = np.trace(a)
            # проверка, что сумма по главной диагонали совпадает с суммой по столбцам
            if np.array_equal(sum_col[0], sum_gd):
                # сумма элементов на побочной диагонали
                sum_pd = np.trace(np.fliplr(a))
                # проверка, что сумма по побочной диагонали совпадает с суммой по столбцам
                if not (np.array_equal(sum_col[0], np.trace(np.fliplr(a)))):
                    f = False
            else:
                f = False
        else:
            f = False
    else:
        f = False
    return f


# Основная программа
a = np.array([[2, 5, 2], [3, 3, 3], [4, 1, 4]])  # магический квадрат
print(mag_matrix(a))

a = np.array([[1, 5, 2], [3, 3, 3], [4, 1, 4]])  # не является магическим квадратом
print(mag_matrix(a))
