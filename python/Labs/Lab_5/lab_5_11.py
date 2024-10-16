import numpy as np
import matplotlib.pyplot as plt

# Установим угол от 0 до 3π/2
phi = np.linspace(0, 3 * np.pi / 2, 100)

# Уравнение кардиоиды: ρ = 2r(1 + cosφ)
r = 2.5 * (1 + np.cos(phi))

# Построение графика в полярной системе координат
plt.polar(phi, r, marker="*", color="green")

# Добавление легенды
plt.legend(["Кардиоида"], title="Функция", loc="upper left")

# Отображение графика
plt.title("График кардиоиды в полярной системе координат")
plt.show()
