import numpy as np

# 1. Создание массива
rows = 5
cols = 5
low = -10
high = 10

matrix = np.random.randint(low, high, size=(rows, cols))
print(matrix)

# 2. Поиск минимального элемента
min_elem = np.min(matrix)
min_index = np.unravel_index(np.argmin(matrix), matrix.shape)
min_row, min_col = min_index

# 3. Удаление строки и столбца
matrix_reduced = np.delete(matrix, min_row, axis=0)  # Удаляем строку
matrix_reduced = np.delete(matrix_reduced, min_col, axis=1)  # Удаляем столбец
print("Массив после удаления строки и столбца:")
print(matrix_reduced)

# 4. Сортировка оставшихся столбцов по неубыванию их минимальных элементов
sorted_indices = np.argsort(np.min(matrix_reduced, axis=0))
matrix_sorted = matrix_reduced[:, sorted_indices]
print("Отсортированный массив по минимальным элементам столбцов:")
print(matrix_sorted)
