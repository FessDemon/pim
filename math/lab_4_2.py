import numpy as np

matrix1 = np.array([[5.2, 3.7, 1.5, 0.5], 
                   [8.1, 9.3, 1.2, 0.75], 
                   [3.6, 8.1, 6.23, 12.5]])

matrix2 = np.array([[4, 5, 1, 15], 
                   [6, 8, 2, 24], 
                   [3, 4, 1, 12]], dtype=float)

matrix3 = np.array([[4.1, 5.2, 3.7, 1.5, 15], 
                   [4.1, 5.2, 3.7, 1.5, 0.5], 
                   [8.1, 9.3, 16, 1.2, 0.75],
                   [3.6, 8.1, 6.23, 4.8, 12.5]])


def makeTrianglePivot(matrix):
    for nrow in range(len(matrix)):
        # nrow равен номеру строки
        # np.argmax возвращает номер строки с максимальным элементом в уменьшенной матрице
        # которая начинается со строки nrow. Поэтому нужно прибавить nrow к результату
        pivot = nrow + np.argmax(abs(matrix[nrow:, nrow]))
        if pivot != nrow:
            # swap
            # matrix[nrow], matrix[pivot] = matrix[pivot], matrix[nrow] - не работает.
            # нужно переставлять строки именно так, как написано ниже
            # matrix[[nrow, pivot]] = matrix[[pivot, nrow]]
            matrix[nrow], matrix[pivot] = matrix[pivot], np.copy(matrix[nrow])
        row = matrix[nrow]
        divider = row[nrow] # диагональный элемент
        if abs(divider) < 1e-10:
            '''
            # почти нуль на диагонали. Продолжать не имеет смысла, результат счёта неустойчив
            '''   
            return 0
        else:
            # делим на диагональный элемент.
            row /= divider
            # теперь надо вычесть приведённую строку из всех нижележащих строчек
            for lower_row in matrix[nrow+1:]:
                factor = lower_row[nrow] # элемент строки в колонке nrow
                lower_row -= factor*row # вычитаем, чтобы получить ноль в колонке nrow
    return matrix


def makeIdentity(matrix):
    # перебор строк в обратном порядке 
    for nrow in range(len(matrix)-1,0,-1):
        row = matrix[nrow]
        for upper_row in matrix[:nrow]:
            factor = upper_row[nrow]
            # вычитать строки не нужно, так как в row только два элемента отличны от 0:
            # в последней колонке и на диагонали
            
            # вычитание в последней колонке
            upper_row[-1] -= factor*row[-1]
            # вместо вычитания 1*factor просто обнулим коэффициент в соотвествующей колонке. 
            upper_row[nrow] = 0
    return matrix


def gaussSolvePivot(A, b=None):
    """Решает систему линейных алгебраических уравнений Ax=b
    Если b is None, то свободные коэффициенты в последней колонке"""
    shape = A.shape
    assert len(shape) == 2, ("Матрица не двумерная", shape) # двумерная матрица
    A = A.copy()
    if b is not None:
        assert shape[0] == shape[1], ("Матрица не квадратная", shape)
        assert b.shape == (shape[0],), ("Размерность свободных членов не соответствует матрице A", shape, b.shape)
        

        # добавляем свободные члены дополнительным столбцом
        A = np.c_[A, b]
    else:
        # Проверяем, что квадратная плюс столбец
        assert shape[0]+1 == shape[1], ("Неверный формат матрицы", shape)
    print('Прямой ход')
    makeTrianglePivot(A)
    print(A)
    if np.linalg.matrix_rank(A) != shape[0]:
        return "Система имеет бесконечно много решений"
    else:
        if np.linalg.matrix_rank(A[:,:-1]) != np.linalg.matrix_rank(A):
            return "Система несовместна"
            
        else:
            print('Обратный ход')
            makeIdentity(A)
            print(A)
            return A[:,-1]
        


print("Ответ: ",gaussSolvePivot(matrix1))

print("Ответ: ",gaussSolvePivot(matrix2))

print("Ответ: ",gaussSolvePivot(matrix3))