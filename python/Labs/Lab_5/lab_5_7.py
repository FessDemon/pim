import numpy as np

# 1. Создание массива
rows, cols = 3, 5
A = np.random.randint(-9, 6, size=(rows, cols))
print("Исходный массив:")
print(A)

# 2. Поиск минимального элемента
min_elem = np.min(A)
min_index = np.unravel_index(np.argmin(A), A.shape)
min_row, min_col = min_index

# 3. Удаление строки и столбца
A_reduced = np.delete(A, min_row, axis=0)  # Удаляем строку
A_reduced = np.delete(A_reduced, min_col, axis=1)  # Удаляем столбец
print("Массив после удаления строки и столбца:")
print(A_reduced)

# 4. Сортировка оставшихся столбцов по неубыванию их минимальных элементов
sorted_indices = np.argsort(np.min(A_reduced, axis=0))
A_sorted = A_reduced[:, sorted_indices]
print("Отсортированный массив по минимальным элементам столбцов:")
print(A_sorted)
