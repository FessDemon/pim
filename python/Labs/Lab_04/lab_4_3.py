original_dict = {
    1: "яблоко",
    2: "банан",
    3: "яблоко",
    4: "апельсин",
    5: "банан"
}

def reverse_dict_items(dict_items):
    reversed_dict = {}

    for key, value in dict_items:
        if value in reversed_dict:
            # Если значение уже есть в новом словаре, добавляем ключ в список
            if isinstance(reversed_dict[value], list):
                reversed_dict[value].append(key)
            else:
                reversed_dict[value] = [reversed_dict[value], key]
        else:
            # Если значения еще нет, добавляем его
            reversed_dict[value] = key

    return reversed_dict

# Получаем dict_items из оригинального словаря
dict_items = original_dict.items()

# Создаем обратный словарь
reversed_dictionary = reverse_dict_items(dict_items)

# Выводим результат
print(reversed_dictionary)