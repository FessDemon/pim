import os
import random

friends_dict = {}


def append_dict_items(friends_dict, name_obj):
    f_dict = friends_dict
    data = []  # формируем список строк файла
    with open(name_obj, "r", encoding="utf-8") as file:
        for line in file:
            data.append(line.strip())
    # Проверка корректности записи в фале
    i = 0
    f = True
    keys = ""
    value = {}
    while f and (i < len(data)):
        if (i == 0) and (data[i] != "Имя"):
            f = False
        elif i == 1:
            keys += data[i]
        elif (i == 2) and (data[i] != ""):
            f = False
        elif (i == 3) and (data[i] != "Фамилия"):
            f = False
        elif i == 4:
            keys += " " + data[i]
        elif (i == 5) and (data[i] != ""):
            f = False
        elif i == 6:
            if data[i] != "Возраст":
                f = False
            else:
                key = data[i]
        elif i == 7:
            value[key] = data[i]
        elif (i == 8) and (data[i] != ""):
            f = False
        elif i == 9:
            if data[i] != "Любимая еда":
                f = False
            else:
                key = data[i]
        elif i == 10:
            value[key] = data[i]
        elif (i == 11) and (data[i] != ""):
            f = False
        elif i == 12:
            if data[i] != "Музыкальная группа":
                f = False
            else:
                key = data[i]
        elif i == 13:
            value[key] = data[i]
        elif (i == 14) and (data[i] != ""):
            f = False
        elif i == 15:
            if data[i] != "Заветная мечта":
                f = False
            else:
                key = data[i]
        elif i == 16:
            value[key] = data[i]
        i += 1
    if i == len(data):  # если запись в фале корректна
        while (keys in friends_dict) and (value != friends_dict[keys]):
            # Если значение уже есть в новом словаре, корректируем keys
            keys = keys + "_"
        # значения еще нет, добавляем его
        f_dict[keys] = value
    return f_dict


# Инициализация рабочего каталога
print("Введите имя каталога, содержащего анкетные файлы:")
name_dir = input()
# name_dir = 'task_2'

# Проверка корректности рабочего каталога
if not (os.path.exists(name_dir)):
    print("Такого каталога не существует. Введите корректно полное имя каталога: ")
    name_dir = input()

# Чтение структуры каталога
for name in os.listdir(name_dir):  # просмотр содержимого каталога
    name_obj = os.path.join(name_dir, name)  # получение полного имени объекта
    if os.path.isfile(name_obj) and (
        name[-4:] == ".txt"
    ):  # если объект - это файл .txt, то
        # Добавление информации из файла в словарь
        friends_dict = append_dict_items(friends_dict, name_obj)

# Формирование массива друзей
friends = []
for key in friends_dict.keys():
    friends.append(key)

f = True  # Идет игра
while f:
    # Выбор случайного друга
    friend_name = friends[random.randint(0, len(friends) - 1)]
    # словарь категорий загаданного человека
    category = friends_dict[friend_name]
    set_categories = set()  # Множество категорий
    categories = []  # Массив категорий
    # Формирование множества и массива категорий
    for key in category.keys():
        categories.append(key)
        set_categories.add(key)

    print("Отгадай загаданного человека по уазанной категории (укажи его Имя Фамилию)")
    while f and (
        set_categories != set()
    ):  # Пока идет игра и не все категрии использованы
        category_name = categories[
            random.randint(0, len(categories) - 1)
        ]  # выбор случайной категории
        # Проверка. что категория не использовалась в текущем раунде игры
        while not (category_name in set_categories):
            category_name = categories[random.randint(0, len(categories) - 1)]
        # вывод категории и ее значения для загаданного человека
        print(category_name, ": ", category[category_name])
        # Если игрок отгадал загаданного человека
        if input() == friend_name:
            print("Ты отгадал!")
            f = False
        else:
            # иначе (если не отгадал),
            # то удаляем из множества отработанную категрию
            set_categories.remove(category_name)
    if f:  # Если все категории выведены, но человек не отгадан
        print(f"Увы... Имя загаданного друга: {friend_name}")
    print("Попробуем еще раз? (да/нет)")
    f = input() == "да"
