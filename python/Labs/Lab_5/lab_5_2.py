import numpy as np

while True:
    try:
        n = int(
            input("Введите положительное целое число для определения "
                  "длины массива (больше 1): ")
        )
        if n > 0:
            break
        else:
            print("Число должно быть больше 0! Попробуйте еще раз.")
    except ValueError:
        print("Некорректный ввод! Попробуйте еще раз.")


def max_after_zero(arr):
    # Преобразуем список в массив NumPy
    np_arr = np.array(arr)

    # Находим индексы элементов, перед которыми стоит ноль
    # Убираем последний элемент для сравнения
    zero_indices = np.where(np_arr[:-1] == 0)[0]

    # Если нет элементов перед которыми стоит ноль
    if zero_indices.size == 0:
        print("Нет элементов перед которыми стоит ноль")
        return

    # Извлекаем элементы, которые идут после нуля
    candidates = np_arr[zero_indices + 1]

    # Возвращаем максимальное значение среди кандидатов
    return print("Максимальный элемент среди тех, перед которыми стоит ноль: "
                 f"{np.max(candidates)}")


print(
    "Введи два числа через пробел - диапазон элементов массива [a, b]",
)
d = input().split()
x = np.random.randint(int(d[0]), int(d[1]) + 1, (n,))
print("x = ", x)

result = max_after_zero(x)
# print(f"Максимальный элемент среди тех, перед которыми стоит ноль: {result}")
