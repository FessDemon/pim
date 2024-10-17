import numpy as np

# Создаем пустую матрицу размером 6x6
matrix = np.zeros((6, 6))

# Первая строка заполняется числами от 1 до 6
matrix[0] = np.arange(1, 7)

# Остальные строки начинаютсья с числа, следующего за максимальным числом предыдущей строки
max_value = matrix[0].max() + 1
for i in range(1, 6):
    next_row = max_value + np.arange(i+1)
    matrix[i] = next_row[:6-(i*2)]
    max_value += len(next_row)
    
print(matrix)