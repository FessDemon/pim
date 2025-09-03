import os


def process_txt_file(src_file, dest_file, depth):
    with open(src_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    line_count = len(lines)

    with open(dest_file, "w", encoding="utf-8") as f:
        f.write(f"{line_count}\n")  # Первая строка - количество строк
        f.writelines(lines)  # Записываем оригинальные строки
        f.write(f"{depth}\n")  # Последняя строка - уровень вложенности


def copy_structure_with_processing(src_dir, dest_dir, depth=0):
    if not os.path.exists(dest_dir):
        # Создаем каталог назначения если он не существует
        os.makedirs(dest_dir)
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)

        if os.path.isdir(src_path):
            copy_structure_with_processing(
                src_path, dest_path, depth + 1
            )  # Рекурсивный вызов для подкаталогов
        elif item.endswith(".txt"):
            # Обработка .txt файлов
            process_txt_file(src_path, dest_path, depth)


source_directory = "python/task_4_4/start"
destination_directory = "python/task_4_4/finish"
copy_structure_with_processing(source_directory, destination_directory)
