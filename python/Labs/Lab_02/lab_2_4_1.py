def remove_parentheses(s):
    stack = []
    result = []

    for char in s:
        if char == "(":
            stack.append(len(result))  # Запоминаем текущую длину результата
        elif char == ")":
            if stack:  # Если есть открывающая скобка
                # Получаем индекс начала вложенной части
                start_index = stack.pop()
                # Удаляем часть строки между скобками
                result = result[:start_index]
        else:
            # Добавляем символы только если нет открывающих скобок
            if not stack:
                result.append(char)

    return "".join(result)


# Пример использования
input_string = "Пример (удалить (это)) строку (с текстом)"
output_string = remove_parentheses(input_string)
print(output_string)
