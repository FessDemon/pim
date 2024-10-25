import datetime


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Проверка числа
# number = 35742549198872617291353508656626642567
# number = 2147483647
number = 11111111111111111111111

start_time = datetime.datetime.now()
result = is_prime(number)
end_time = datetime.datetime.now()

print(f"Число {number} {'простое' if result else 'составное'}")
print(f"Время выполнения (без обработки исключений): {end_time - start_time} секунд")
