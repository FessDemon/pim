class Apartment:
    def __init__(self, address, price, rooms, area):
        self.address = address
        self.price = price
        self.rooms = rooms
        self.area = area
        self.is_available = True

    def rent(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def __str__(self):
        availability = "Доступна" if self.is_available else "Не доступна"
        return f"Квартира по {self.address}: {self.rooms} комнат, {self.area}m², Цена: {self.price}, Статус: {availability}"


class Tenant:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def can_afford(self, apartment):
        return self.budget >= apartment.price

    def __str__(self):
        return f"Арендатор: {self.name}, Budget: {self.budget}"


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
                print(f"{tenant.name} has rented the apartment at {apartment.address}.")
            else:
                print("Apartment is not available.")
        else:
            print("Apartment cannot be rented.")


def main():
    agency = Agency()

    # Добавление квартир в агентство
    agency.add_apartment(Apartment("123 Main St", 1000, 2, 50))
    agency.add_apartment(Apartment("456 Elm St", 800, 1, 30))
    agency.add_apartment(Apartment("789 Oak St", 1200, 3, 70))

    # Создание квартиросъемщиков
    tenants = {}

    while True:
        print("\nWelcome to the Housing Agency!")
        print("1. Register as a new tenant")
        print("2. Search for apartments")
        print("3. Rent an apartment")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            name = input("Enter your name: ")
            budget = float(input("Enter your budget: "))
            tenants[name] = Tenant(name, budget)
            print(f"Tenant {name} registered successfully.")

        elif choice == "2":
            name = input("Enter your name to search for apartments: ")
            if name in tenants:
                tenant = tenants[name]
                print(f"\nAvailable apartments for {tenant.name}:")
                available_apartments = agency.find_apartments(tenant)
                if available_apartments:
                    for apt in available_apartments:
                        print(apt)
                else:
                    print("No available apartments within your budget.")
            else:
                print("Tenant not found. Please register first.")

        elif choice == "3":
            name = input("Enter your name to rent an apartment: ")
            if name in tenants:
                tenant = tenants[name]
                address = input("Enter the address of the apartment you want to rent: ")
                apartment_to_rent = next(
                    (apt for apt in agency.apartments if apt.address == address), None
                )

                if apartment_to_rent:
                    agency.rent_apartment(tenant, apartment_to_rent)
                else:
                    print("Apartment not found.")
            else:
                print("Tenant not found. Please register first.")

        elif choice == "4":
            print("Thank you for using the Housing Agency system. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
