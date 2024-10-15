import os
import random


# Функция для загрузки данных из файлов
def load_data(directory):
    friends = {}
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                data = {}
                lines = file.readlines()
                for i in range(0, len(lines), 2):
                    key = lines[i].strip()
                    value = lines[i + 1].strip()
                    data[key] = value
                name = f"{data['Имя']} {data['Фамилия']}"
                friends[name] = data
    return friends


# Функция для игры
def play_game(friends):
    while True:
        friend_name = random.choice(list(friends.keys()))
        friend_data = friends[friend_name]

        # Убираем имя и фамилию из категорий
        categories = list(friend_data.keys())
        categories.remove('Имя')
        categories.remove('Фамилия')

        # Случайный выбор категории
        category = random.choice(categories)
        value = friend_data[category]

        print(f"\nЗначение: {value}")

        # Угадывание друга
        guess = input("Кто это? (введите имя и фамилию или 'выход' для завершения): ")

        if guess.lower() == 'выход':
            print("Спасибо за игру!")
            break

        if guess == friend_name:
            print("Правильно! Вы угадали.")
        else:
            print(f"Неправильно. Это был {friend_name}.")

        # Спрашиваем, хотим ли мы продолжить
        continue_playing = input("Хотите загадать другого друга? (да/нет): ")
        if continue_playing.lower() != 'да':
            print("Спасибо за игру!")
            break


# Основная часть программы
directory_path = "task_4_2"
friends_data = load_data(directory_path)
play_game(friends_data)