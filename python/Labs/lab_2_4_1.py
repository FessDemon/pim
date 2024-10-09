def remove_parentheses(s):
    stack = []
    result = []
    
    for char in s:
        if char == '(':
            stack.append(len(result))  # Запоминаем текущую длину результата
        elif char == ')':
            if stack:  # Если есть открывающая скобка
                start_index = stack.pop()  # Получаем индекс начала вложенной части
                result = result[:start_index]  # Удаляем часть строки между скобками
        else:
            if not stack:  # Добавляем символы только если нет открывающих скобок
                result.append(char)

    return ''.join(result)

# Пример использования
input_string = "Пример (удалить (это)) строку (с текстом)"
output_string = remove_parentheses(input_string)
print(output_string)  # Вывод: "Пример  строку "