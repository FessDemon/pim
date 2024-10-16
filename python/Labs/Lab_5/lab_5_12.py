import numpy as np
import matplotlib.pyplot as plt


def get_color():
    """Функция выбора цвета графика"""
    colors = {1: "red", 2: "blue", 3: "green", 4: "orange", 5: "purple"}
    print("Выберите цвет графика:")
    for key, value in colors.items():
        print(f"{key}. {value}")

    while True:
        try:
            choice = int(input("Введите номер цвета (1-5): "))
            if choice in colors:
                return colors[choice]
            else:
                print("Некорректный выбор. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите число.")


def get_line_style():
    """Функция выбора типа линии графика"""
    line_styles = {1: "-", 2: "--", 3: "-."}
    print("Выберите тип линии:")
    for key, value in line_styles.items():
        print(f"{key}. {value}")

    while True:
        try:
            choice = int(input("Введите номер типа линии (1-3): "))
            if choice in line_styles:
                return line_styles[choice]
            else:
                print("Некорректный выбор. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите число.")


def get_line_width():
    """Функция выбора толщины линии графика"""
    widths = [1, 2, 3, 4, 5]
    print("Выберите толщину линии:")
    for i, width in enumerate(widths):
        print(f"{i + 1}. {width}")

    while True:
        try:
            choice = int(input("Введите номер толщины линии (1-5): "))
            if 1 <= choice <= len(widths):
                return widths[choice - 1]
            else:
                print("Некорректный выбор. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите число.")


def plot_graph(color, line_style, line_width):
    """Функция отрисовки графика"""
    x = np.linspace(0, 10, 100)
    y = np.sqrt(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color=color, linestyle=line_style, linewidth=line_width)

    plt.title(r"График функции $y=\sqrt{x}$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(0, 10)
    plt.ylim(0, 3.5)
    plt.grid()
    plt.axhline(0, color="black", linewidth=0.5, ls="--")
    plt.axvline(0, color="black", linewidth=0.5, ls="--")

    plt.show()


def main():
    color = get_color()
    line_style = get_line_style()
    line_width = get_line_width()

    plot_graph(color, line_style, line_width)


if __name__ == "__main__":
    main()
