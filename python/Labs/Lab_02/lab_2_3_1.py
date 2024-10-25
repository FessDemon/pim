inputString = '55ttppi'
if inputString == '':
        print('Строка пустая.')
else:
    result = [] 
    currentChar = inputString[0]  # Первый символ строки
    result.append(currentChar)  # Добавляем первый символ в результат
    
    for char in inputString[1:]:
        if char != currentChar:  # Если текущий символ отличается от предыдущего
            result.append('*')  # Добавляем разделитель
            currentChar = char  # Обновляем текущий символ
        result.append(char)  # Добавляем текущий символ в результат

print(''.join(result))
