def fix_punctuation(text):
    # Знаки препинания, которые требуют обработки
    punctuation = {'.', ',', ';', ':', '!', '?', '(', '[', '{', ')', ']', '}', '-'}
    result = []
    i = 0

    while i < len(text):
        char = text[i]

        # Удаляем пробелы перед знаками препинания (кроме тире и открывающихся скобок)
        if char in punctuation:
            if char in {')', ']', '}', '-'}:
                # Удаляем пробел перед закрывающей скобкой
                if result and result[-1] == ' ':
                    result.pop()
            # elif char == '-':
            #     # Удаляем пробел перед тире
            #     if result and result[-1] == ' ':
            #         result.pop()
            else:
                # Удаляем пробел перед другими знаками
                if result and result[-1] == ' ':
                    result.pop()
                result.append(char)

            # Добавляем пробел после знака, если это не открывающая скобка
            if char not in {'(', '[', '{'}:
                # Пропускаем все последующие пробелы
                while i + 1 < len(text) and text[i + 1] == ' ':
                    i += 1
                result.append(' ')
        else:
            # Добавляем символ в результат
            if char != ' ' or (result and result[-1] != ' '):  # Убираем лишние пробелы
                result.append(char)

        i += 1

    # Обработка многоточия
    final_result = []
    dot_count = 0

    for char in result:
        if char == '.':
            dot_count += 1
        else:
            if dot_count > 0:
                final_result.append('.')
                if dot_count > 1:  # Если было больше одной точки, добавляем многоточие
                    final_result.append('.' * (dot_count - 1))
                dot_count = 0
            final_result.append(char)

    # Удаляем лишние пробелы в конце строки и возвращаем результат
    return ''.join(final_result).strip()

# Пример использования
input_text = "Это пример текста , который содержит           неправильные  -знаки препинания .   Надо   исправить   его !   И вот так ...   ( например )   "
fixed_text = fix_punctuation(input_text)
print(fixed_text)
