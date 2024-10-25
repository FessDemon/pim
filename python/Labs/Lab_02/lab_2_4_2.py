import re


def remove_parentheses(s):
    # Регулярное выражение для поиска текста между круглыми скобками
    pattern = r"\([^()]*\)"  # Находим текст в скобках без вложенных скобок
    while re.search(pattern, s):  # Повторяем, пока есть совпадения
        # Заменяем найденные совпадения на пустую строку
        s = re.sub(pattern, "", s)
    return s.strip()  # Удаляем лишние пробелы в начале и конце строки


# Пример использования
input_string = "9((j)())9((()j))9"
output_string = remove_parentheses(input_string)
print(output_string)
