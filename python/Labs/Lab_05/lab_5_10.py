import matplotlib.pyplot as plt


# Функция для чтения данных из файла
def read_precipitation_data(file_path):
    months = []
    precipitation = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            month, value = line.split()
            months.append(month)
            precipitation.append(int(value))
    return months, precipitation


# Чтение данных из файла
file_path = "python/Labs/Lab_5/task_5_10/data.txt"
months, precipitation = read_precipitation_data(file_path)

# Создание фигуры и осей
fig, axs = plt.subplots(3, 1, figsize=(15, 20))

# Обычная столбиковая диаграмма
axs[0].bar(months, precipitation, color="blue")
axs[0].set_title("Столбиковая диаграмма осадков")
axs[0].set_ylabel("Количество осадков (мм)")

# Горизонтальная диаграмма
axs[1].barh(months, precipitation, color="green")
axs[1].set_title("Горизонтальная диаграмма осадков")
axs[1].set_xlabel("Количество осадков (мм)")

# Круговая диаграмма
axs[2].pie(precipitation, labels=months, autopct="%1.1f%%", startangle=140)
axs[2].set_title("Круговая диаграмма осадков")

# Настройка общего заголовка
plt.suptitle("Годовое количество осадков по месяцам")

# Сохранение рисунка в файл
plt.savefig("python/Labs/Lab_5/task_5_10/diagrams.png")

# Показать график
plt.show()
