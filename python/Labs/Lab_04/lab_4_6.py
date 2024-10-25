import os
import re

# Инициализация рабочего каталога
print("Введите имя каталога, содержащего файл input.txt:")
name_dir = input()

# Проверка корректности рабочего каталога
if not (os.path.exists(name_dir)):
    print("Такого каталога не существует. Введите корректно полное имя каталога: ")
    name_dir = input()

input_file_1 = name_dir + "/shop1.txt"
input_file_2 = name_dir + "/shop2.txt"
output_file = name_dir + "/shop_max.txt"

# Проверка входного файла shop1.txt
while not (os.path.exists(input_file_1)):
    print(
        "Файла shop1.txt  в указанном каталоге не существует."
        "Введите корректно полное имя входного файла: "
    )
    input_file_1 = input()

# Проверка входного файла shop2.txt
while not (os.path.exists(input_file_2)):
    print(
        "Файла shop2.txt  в указанном каталоге не существует."
        "Введите корректно полное имя входного файла: "
    )
    input_file_2 = input()

# Словарь для хранения прайс-листов
prices_dict = {}


# Функция для очистки строки от мусора
def clean_line(line):
    # Регулярное выражение ищет строку формата
    # "название товара - цена", где цена — это число
    match = re.match(r"(.+?)\s*-\s*(\d+)", line)
    if match:
        name = match.group(1).strip()  # Убираем лишние пробелы вокруг названия
        price = match.group(2)  # Получаем цену
        return name, price
    return None


# Открываем 1-ый файл для чтения
with open(input_file_1, "r", encoding="utf-8") as file:
    for line in file:
        result = clean_line(line.rstrip())  # Очищаем строку
        if result:
            name, price = result
            prices_dict[name] = price


# Открываем 2-ый файл для чтения
with open(input_file_2, "r", encoding="utf-8") as file:
    for line in file:
        result = clean_line(line.rstrip())
        if result:
            name, price = result
            if name not in prices_dict:
                prices_dict[name] = price
            else:
                prices_dict[name] = max(prices_dict[name], price)


def write_to_file(filename, data):
    """Записывает данные в файл."""
    with open(filename, "w", encoding="utf-8") as file:
        for name, price in sorted(data.items()):
            file.write(f"{name} – {price}\n")
    print(f"Файл {filename} успешно записан.")


# Проверка существования файла
if os.path.exists(output_file):
    print(
        f"Файл {output_file} в указанном каталоге уже существует. Введите OK, если хотите переписать имеющийся файл, или введите любое другое значение для отмены: "
    )
    is_read = input()
    if is_read != "OK":
        print("Перезапись файла отменена.")
    else:
        # Перезапись файла
        write_to_file(output_file, prices_dict)
else:
    # Если файла нет, то записываем данные в новый файл
    write_to_file(output_file, prices_dict)
