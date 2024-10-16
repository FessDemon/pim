import os
import matplotlib.pyplot as plt
from collections import Counter
import string


def load_texts(directory):
    texts = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), "r", encoding="utf-8") as file:
                texts.append(file.read())
    return texts


def select_text(texts, index):
    if 0 <= index < len(texts):
        return texts[index]
    else:
        raise IndexError("Index out of range.")


def preprocess_text(text):
    # Приведение к нижнему регистру и удаление знаков препинания
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text


def plot_word_frequency(text):
    words = preprocess_text(text).split()

    # Фильтрация коротких слов (менее 3 символов)
    filtered_words = [word for word in words if len(word) > 3]

    word_counts = Counter(filtered_words)

    # Получение 50 наиболее частых слов
    most_common_words = word_counts.most_common(50)

    # Разделение на слова и их частоты
    words, counts = zip(*most_common_words)

    plt.figure(figsize=(12, 8))
    plt.barh(words, counts, color="skyblue")
    plt.xlabel("Частота")
    plt.title("Частота 50 наиболее употребляемых слов")
    plt.gca().invert_yaxis()  # Инвертировать ось Y для лучшего отображения
    plt.show()


def main():
    directory = "python/Labs/Lab_5/task_5_9/text"  # Папка с текстами
    texts = load_texts(directory)

    print("Выберите текст по индексу (0 - {}):".format(len(texts) - 1))
    for i in range(len(texts)):
        print(f"{i}: Текст {i + 1}")

    index = int(input("Введите индекс текста: "))

    try:
        selected_text = select_text(texts, index)
        plot_word_frequency(selected_text)
    except IndexError as e:
        print(e)


if __name__ == "__main__":
    main()
