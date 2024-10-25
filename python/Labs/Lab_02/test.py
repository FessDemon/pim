# Чтение англо-русского словаря из файла
input_file = 'task_4_1/input.txt'
output_file = 'task_4_1/output.txt'

# Словарь для хранения русско-английских переводов
rus_eng_dict = {}

# Открываем файл для чтения
with open(input_file, 'r', encoding='utf-8') as file:
    for line in file:
        # Разделяем строку на английское слово и русские переводы
        eng_word, rus_words = line.strip().split(' – ')
        rus_words_list = [word.strip() for word in rus_words.split(',')]

        # Заполняем русско-английский словарь
        for rus_word in rus_words_list:
            if rus_word not in rus_eng_dict:
                rus_eng_dict[rus_word] = []
            rus_eng_dict[rus_word].append(eng_word)

# Сортируем словарь по ключам (русским словам)
sorted_rus_eng_dict = dict(sorted(rus_eng_dict.items()))

# Записываем результат в выходной файл
with open(output_file, 'w', encoding='utf-8') as file:
    for rus_word, eng_words in sorted_rus_eng_dict.items():
        file.write(f"{rus_word} – {', '.join(eng_words)}\n")

print("Русско-английский словарь успешно создан и сохранен в output.txt.")