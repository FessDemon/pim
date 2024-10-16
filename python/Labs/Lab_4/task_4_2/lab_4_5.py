import os
import time
import shutil


def solve(dir):
    for name in os.listdir(dir):  # просмотр содержимого каталога
        path = os.path.join(dir, name)  # получение полного имени объекта
        if os.path.isfile(path):  # если объект - это файл, то
            ctime = os.path.getctime(
                path
            )  # получение информации о дате и времени создания файла
            date = str(
                time.ctime(ctime)
            ).split()  # разбивка даты и времени на составляющие
            date = (
                date[3],
                date[2],
                date[1],
                date[4],
            )  # формирование даты в формате время день месяц год
            new_dir = " ".join(date)  # склейка даты в строку
            new_path = dir + new_dir + "/"  # формирование имени нового каталога
            if not (new_dir in os.listdir(dir)):  # если такого каталога еще нет, то
                os.mkdir(new_path)  # создание каталога с датой создания файла
            shutil.move(path, new_path + name)  # перемещение файла в новый каталог


# full_name_dir = 'e:/0/'

# ввод каталога с проверкой корректности ввода
print("Введите полное имя каталога: ")
full_name_dir = input()
while not (os.path.exists(full_name_dir)):
    print("Такого каталога не существует. Введите корректно полное имя каталога: ")
    full_name_dir = input()
solve(full_name_dir)
print("Файлы успешно переписаны")
