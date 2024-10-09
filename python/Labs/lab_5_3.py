import numpy as np

# mass = np.array([[4, 5, 6], [2, 9, 0], [4, 0, 7]])
# print(mass)


def generate_integer_matrix(rows, cols, low, high):
    matrix = np.random.randint(low, high, size=(rows, cols))
    return matrix


rows = 5  # Количество строк
cols = 5  # Количество столбцов
low = -5  # Нижняя граница
high = 5  # Верхняя граница

matrix = generate_integer_matrix(rows, cols, low, high)
print(matrix)


# Для первого условия
print("количество строк, не содержащих ни одного нулевого элемента")
print(sum(0 not in x for x in matrix))

# Для второго условия
print(
    "максимальное значение из чисел, встречающихся в заданной матрице более одного раза"
)
print(max([x for i in [[x for a in matrix for x in a]] for x in i if i.count(x) > 1]))
