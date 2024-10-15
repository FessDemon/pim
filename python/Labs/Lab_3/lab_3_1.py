# Список кортежей с именами и номерами комнат
hotel_rooms = [('Ann', 400), ('Elizabeth', 103), ('Mr McMullen', 202), ('Mrs Smith', 200)]

# Перебираем каждый элемент в списке
for name, room in hotel_rooms:
    # Проверяем, содержит ли имя титул
    if name.startswith('Mr') or name.startswith('Mrs') or name.startswith('Ms') or name.startswith('Miss'):
        print(f"Good morning, {name}! Your room is {room}.")
    else:
        print(f"Hello, {name}! Your room is {room}.")
