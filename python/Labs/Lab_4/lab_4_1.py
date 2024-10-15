import os
import re

# Инициализация рабочего каталога
print("Введите имя каталога, содержащего файл input.txt:")
name_dir = input()
# name_dir = 'task_4_1'

# Проверка корректности рабочего каталога
if not (os.path.exists(name_dir)):
    print("Такого каталога не существует. Введите корректно полное имя каталога: ")
    name_dir = input()

# Инициализация файлов
input_file = name_dir + "/input.txt"
output_file = name_dir + "/output.txt"

# Проверка входного файла
while not (os.path.exists(input_file)):
    print(
        "Файла input.txt  в указанном каталоге не существует. Введите корректно полное имя входного файла: "
    )
    input_file = input()

# Словарь для хранения русско-английских переводов
rus_eng_dict = {}

# Чтение англо-русского словаря из файла
if os.stat(input_file).st_size == 0:
    print("Файл словаря пуст")
else:
    # Открываем файл для чтения
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            # Убираем лишние символы и пробелы с краев строки
            clean_line = re.sub(r"[^\w\s–,]", "", line).strip()

            # Проверка, содержит ли строка цифры
            if re.search(r"\d", clean_line):
                # Удаляем цифры из строки, оставляя только буквы
                clean_line = re.sub(r"\d+", "", clean_line).strip()

            # Разделяем строку на английское слово и русские переводы
            if " – " in clean_line:
                eng_word, rus_words = clean_line.split(" – ", 1)
                # Очищаем список русских переводов от лишних пробелов и мусорных символов
                rus_words_list = [
                    re.sub(r"[^\w\s]", "", word.strip())
                    for word in rus_words.split(",")
                    if word.strip()
                ]

                # Заполняем русско-английский словарь
                for rus_word in rus_words_list:
                    if rus_word not in rus_eng_dict:
                        rus_eng_dict[rus_word] = []
                    rus_eng_dict[rus_word].append(eng_word)

    # Сортируем словарь по ключам (русским словам)
    sorted_rus_eng_dict = dict(sorted(rus_eng_dict.items()))

    # Записываем результат в выходной файл
    with open(output_file, "w", encoding="utf-8") as file:
        for rus_word, eng_words in sorted_rus_eng_dict.items():
            file.write(f"{rus_word} – {', '.join(eng_words)}\n")

    print("Русско-английский словарь успешно создан и сохранен в output.txt.")
