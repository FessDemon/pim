import numpy as np


def generate_array_method1(n, m):
    """Создает массив размером n x m согласно первому способу."""
    # Создаем пустой массив размером n x m
    array = np.zeros((n, m), dtype=np.int)

    # Заполняем первые две строки
    for i in range(m):
        array[0][i] = i + 1
        array[1][i] = 2 * (i + 1) + 1

    # Заполняем остальные строки
    k = 2
    while k < n:
        j = 0
        while j < m and j + k < m:
            array[k][j] = array[k - 2][j + k]
            j += 1

        if j == m:
            break

        for l in range(k + 1, m):
            array[k][l] = l + 1

        k += 1

    return array


def generate_array_method2(n, m):
    """Создает массив размером n x m согласно второму способу."""
    # Создаем массив с последовательными числами от 1 до n * m
    array = np.arange(1, n * m + 1).reshape(n, m)

    # Переставляем элементы массива в обратном порядке
    for i in range(n // 2):
        array[[i], [m - 1 - i]] = array[[m - 1 - i], [i]]
        array[[n - 1 - i], [m - 1 - i]] = array[[m - 1 - i], [n - 1 - i]]
        array[[n - 1 - i], [i]] = array[[i], [n - 1 - i]]

    return array


import numpy as np


def save_array_as_text(matrix, filename):
    """Сохраняет массив в виде текста в файл."""
    with open(filename, "w", encoding="utf-8") as file:
        for row in matrix:
            for element in row:
                file.write(str(element) + " ")
            file.write("\n")


# Пример использования функции
n = 6
m = 6
method_num = 1

if method_num == 1:
    arr = generate_array_method1(n, m)
elif method_num == 2:
    arr = generate_array_method2(n, m)
else:
    raise ValueError("Метод должен быть равен 1 или 2")

save_array_as_text(arr, f"result_{n}_{m}.txt")
print("Результат успешно сохранен в файл result_{n}_{m}.txt")
