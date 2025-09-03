inputString = "55ttppi"
if inputString == "":
    print("Строка пустая.")
else:
    result = []
    currentChar = inputString[0]  # Первый символ строки
    result.append(currentChar)  # Добавляем первый символ в результат

    for char in inputString[1:]:
        # Если текущий символ отличается от предыдущего
        if char != currentChar:
            result.append("*")  # Добавляем разделитель
            currentChar = char  # Обновляем текущий символ
        result.append(char)  # Добавляем текущий символ в результат

print("".join(result))
