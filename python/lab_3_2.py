def findLongestDecreasingSequences(numbers):
    if not numbers:
        return [], 0, []

    longestSequences = []
    maxLength = 0
    currentSequence = []

    for i in range(len(numbers)):
        if i == 0 or numbers[i] < numbers[i - 1]:
            currentSequence.append(numbers[i])
        else:
            if len(currentSequence) > maxLength:
                maxLength = len(currentSequence)
                longestSequences = [currentSequence]
            elif len(currentSequence) == maxLength:
                longestSequences.append(currentSequence)
            currentSequence = [numbers[i]]

    # Проверка последней последовательности
    if len(currentSequence) > maxLength:
        longestSequences = [currentSequence]
        maxLength = len(currentSequence)
    elif len(currentSequence) == maxLength:
        longestSequences.append(currentSequence)

    return longestSequences, maxLength

# Пример использования
numbers = [9, 7, 5, 6, 4, 3, 2, 1, 8, 7, 9, 7, 5, 3, 2]
longestSequences, maxLength = findLongestDecreasingSequences(numbers)

# Вывод результатов
print("Список чисел:", numbers)
print("Длина самой длинной упорядоченной по убыванию последовательности:", maxLength)
print("Самые длинные последовательности:")

for seq in longestSequences:
    print(seq)
