class Apartment:
    def __init__(self, address, price, rooms, area):
        self.__dict__["address"] = address
        self.__dict__["price"] = price
        self.__dict__["rooms"] = rooms
        self.__dict__["area"] = area
        self.is_available = True

    def __del__(self):
        print(f"Квартира по адресу {self.address} была удалена.")

    def rent(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def __str__(self):
        availability = "Доступна" if self.is_available else "Недоступна"
        return f"Квартира по адресу {self.address}: {self.rooms} комнат(ы), {self.area} м², Цена: {self.price}, Статус: {availability}"

    def __eq__(self, other):
        if isinstance(other, Apartment):
            return self.address.lower() == other.address.lower()
        return NotImplemented

    def __hash__(self):
        return hash(self.address.lower())


class LuxuryApartment(Apartment):
    def __init__(self, address, price, rooms, area, amenities):
        super().__init__(
            address, price, rooms, area
        )  # Вызов конструктора родительского класса
        self.amenities = amenities  # Дополнительные удобства

    def __str__(self):
        base_info = super().__str__()  # Получаем строку из родительского класса
        amenities_info = f", Удобства: {', '.join(self.amenities)}"
        return base_info + amenities_info


class Tenant:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def can_afford(self, apartment):
        return self.budget >= apartment.price

    def __str__(self):
        return f"Квартиросъемщик: {self.name}, Бюджет: {self.budget}"

    def __call__(self):
        return f"Квартиросъемщик {self.name} с бюджетом {self.budget}"


class Agency:
    def __init__(self):
        self.apartments = []

    def add_apartment(self, apartment):
        self.apartments.append(apartment)

    def find_apartments(self, tenant):
        available_apartments = [
            apt
            for apt in self.apartments
            if apt.is_available and tenant.can_afford(apt)
        ]
        return available_apartments

    def rent_apartment(self, tenant, apartment):
        if (
            apartment in self.apartments
            and apartment.is_available
            and tenant.can_afford(apartment)
        ):
            if apartment.rent():
                print(
                    f"{tenant.name} арендовал(а) квартиру по адресу {apartment.address}."
                )
            else:
                print("Квартира недоступна.")
        else:
            print("Квартиру нельзя арендовать.")

    # Методы для работы с квартирами
    def __len__(self):
        return sum(1 for apt in self.apartments if apt.is_available)

    def __getitem__(self, index):
        """Возвращает квартиру по индексу."""
        try:
            return self.apartments[index]
        except IndexError:
            print(f"Квартира с индексом {index} не найдена.")
            return None

    def __setitem__(self, index, apartment):
        self.apartments[index] = apartment

    def __delitem__(self, index):
        del self.apartments[index]

    def __contains__(self, apartment):
        return apartment in self.apartments

    # Новый метод для поиска квартиры по индексу
    def get_apartment_by_index(self, index):
        return self[index]


def main():
    agency = Agency()

    # Добавление квартир в агентство
    agency.add_apartment(Apartment("Улица 1, дом 1", 1000, 2, 50))
    agency.add_apartment(
        LuxuryApartment(
            "Улица 2, дом 2",
            2000,
            3,
            80,
            amenities=["Бассейн", "Сауна", "Фитнес-центр"],
        )
    )
    agency.add_apartment(Apartment("Улица 3, дом 3", 1200, 3, 70))
    agency.add_apartment(Apartment("Улица 3, дом 4", 700, 2, 40))
    agency.add_apartment(Apartment("Улица 3, дом 3", 500, 1, 30))

    # Создание квартиросъемщиков
    tenants = {}

    while True:
        print("\nДобро пожаловать в Жилищное Агентство!")
        print("1. Зарегистрироваться как новый квартиросъемщик")
        print("2. Найти квартиры")
        print("3. Арендовать квартиру")
        print("4. Поиск квартиры по индексу")
        print("5. Показать общее количество доступных квартир")
        print("6. Вывести информацию о квартире по индексу")
        print("7. Выйти")

        choice = input("Выберите опцию (1-7): ")

        if choice == "1":
            name = input("Введите ваше имя: ")
            budget = float(input("Введите ваш бюджет: "))
            tenants[name.lower()] = Tenant(
                name, budget
            )  # Сохраняем имя в нижнем регистре
            print(f"Квартиросъемщик {name} успешно зарегистрирован.")

        elif choice == "2":
            name = input(
                "Введите ваше имя для поиска квартир: "
            ).lower()  # Приводим к нижнему регистру
            if name in tenants:
                tenant = tenants[name]
                print(f"\nДоступные квартиры для {tenant.name}:")
                available_apartments = agency.find_apartments(tenant)
                if available_apartments:
                    for index, apt in enumerate(available_apartments):
                        print(f"{index}: {apt}")
                else:
                    print("Нет доступных квартир в пределах вашего бюджета.")
            else:
                print(
                    "Квартиросъемщик не найден. Пожалуйста, зарегистрируйтесь сначала."
                )

        elif choice == "3":
            name = input(
                "Введите ваше имя для аренды квартиры: "
            ).lower()  # Приводим к нижнему регистру
            if name in tenants:
                tenant = tenants[name]
                available_apartments = agency.find_apartments(tenant)

                if available_apartments:
                    print("\nДоступные квартиры для аренды:")
                    for index, apt in enumerate(available_apartments):
                        print(f"{index}: {apt}")

                    index_to_rent = int(input("Введите индекс квартиры для аренды: "))
                    apartment_to_rent = agency.get_apartment_by_index(index_to_rent)

                    if apartment_to_rent and apartment_to_rent.is_available:
                        agency.rent_apartment(tenant, apartment_to_rent)
                    else:
                        print("Квартира недоступна или не найдена.")
                else:
                    print("Нет доступных квартир в пределах вашего бюджета.")
            else:
                print(
                    "Квартиросъемщик не найден. Пожалуйста, зарегистрируйтесь сначала."
                )

        elif choice == "4":
            index = int(input("Введите индекс квартиры для поиска: "))
            apartment = agency.get_apartment_by_index(index)
            if apartment:
                print(f"Найдена квартира: {apartment}")

        elif choice == "5":
            total_available = len(agency)
            print(f"Общее количество доступных квартир: {total_available}")

        elif choice == "6":
            index = int(input("Введите индекс квартиры для вывода информации: "))
            apartment_info = agency[index]
            if apartment_info:
                print(f"Информация о квартире: {apartment_info}")

        elif choice == "7":
            print("Спасибо за использование системы Жилищного Агентства. До свидания!")
            break

        else:
            print("Неверная опция. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
