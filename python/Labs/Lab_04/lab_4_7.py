import os


def load_data(filename):
    data = {}
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                country, product, amount = line.strip().split(", ")
                amount = int(amount)
                if country not in data:
                    data[country] = {}
                if product in data[country]:
                    data[country][product] += amount
                else:
                    data[country][product] = amount
    return data


def save_data(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        for country in data:
            for product in data[country]:
                file.write(f"{country}, {product}, {data[country][product]}\n")


def add_data(data):
    country = input("Введите название страны: ")
    product = input("Введите название товара: ")
    amount = int(input("Введите объем экспортируемого товара (в тоннах): "))

    if country not in data:
        data[country] = {}

    if product in data[country]:
        data[country][product] += amount
    else:
        data[country][product] = amount

    print("Данные добавлены успешно.")


def display_all(data):
    for country in data:
        for product in data[country]:
            print(f"{country}, {product}, {data[country][product]}")


def products_by_country(data):
    country = input("Введите название страны: ")
    if country in data:
        for product in data[country]:
            print(f"{product}: {data[country][product]} тонн")
    else:
        print("Страна не найдена.")


def countries_by_product(data):
    product = input("Введите название товара: ")
    found = False
    for country in data:
        if product in data[country]:
            print(f"{country}: {data[country][product]} тонн")
            found = True
    if not found:
        print("Товар не найден.")


def main():
    filename = "python/Labs/Lab_4/task_4_7/input.txt"
    data = load_data(filename)

    while True:
        print("\nВыберите действие:")
        print("1. Добавить данные")
        print("2. Вывести всю информацию")
        print("3. Вывести список товаров экспортируемых страной")
        print("4. Вывести список стран экспортирующих товар")
        print("5. Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            add_data(data)
            save_data(filename, data)
        elif choice == "2":
            display_all(data)
        elif choice == "3":
            products_by_country(data)
        elif choice == "4":
            countries_by_product(data)
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
