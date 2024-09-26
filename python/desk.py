import matplotlib.pyplot as plt
import numpy as np

def draw_chess_board():
    # Создаем матрицу 8x8, где 0 - белая клетка, 1 - черная клетка
    board = np.zeros((8, 8))
    board[1::2, ::2] = 1  # Черные клетки на четных строках
    board[::2, 1::2] = 1  # Черные клетки на нечетных строках

    plt.imshow(board, cmap='gray', extent=[0, 8, 0, 8])
    plt.xticks(np.arange(0.5, 8.5), range(1, 9))
    plt.yticks(np.arange(0.5, 8.5), range(1, 9))
    plt.grid(False)
    plt.gca().invert_yaxis()  # Инвертируем ось Y для правильного отображения
    plt.title('Шахматная доска')
    plt.show()

draw_chess_board()
