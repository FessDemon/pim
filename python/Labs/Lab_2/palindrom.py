import re

def is_palindrome(word):
    # Убираем пробелы и приводим к нижнему регистру
    cleaned_word = re.sub(r'[^a-zA-Z0-9]', '', word).lower()
    return cleaned_word == cleaned_word[::-1]

def find_palindromes(text):
    # Разбиваем текст на слова
    words = text.split()
    palindromes = []

    for word in words:
        if is_palindrome(word):
            palindromes.append(word)

    return palindromes

# Пример использования
text = "Шабаш кок ПОП каЗАк шаБаш кОК поп поп рок аа"
palindromes = find_palindromes(text)

print("Найденные палиндромы:", palindromes)
