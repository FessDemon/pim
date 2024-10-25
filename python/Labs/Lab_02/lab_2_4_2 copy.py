import re

inputString = "9((j)())9((()j))9"
pattern = r'\([^()]*\)'  # Находим текст в скобках без вложенных скобок
while re.search(pattern, inputString):  # Повторяем, пока есть совпадения
    inputString = re.sub(pattern, '', inputString)  # Заменяем найденные совпадения на пустую строку

print(inputString.strip())
