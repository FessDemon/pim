import numpy as np

# matrix = np.array([[4, 5, 6], [2, 9, 0], [4, 0, 7]])
# print(matrix)


def generate_integer_matrix(rows, cols, low, high):
    matrix = np.random.randint(low, high, size=(rows, cols))
    return matrix


rows = 5  # Количество строк
cols = 5  # Количество столбцов
low = -10  # Нижняя граница
high = 10  # Верхняя граница

matrix = generate_integer_matrix(rows, cols, low, high)
print(matrix)

# **Определение количества строк без нулевых элементов**
non_zero_rows_count = np.sum(~np.any(matrix == 0, axis=1))

# **Поиск максимального значения среди чисел, встречающихся более одного раза**
unique, counts = np.unique(matrix, return_counts=True)
max_value_multiple_occurrences = (
    unique[counts > 1].max() if np.any(counts > 1) else None
)

print(f"Количество строк без нулевых элементов: {non_zero_rows_count}")
print(
    "Максимальное значение из чисел, встречающихся более одного раза:"
    f"{max_value_multiple_occurrences}"
)
