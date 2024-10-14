import time


def is_prime(n):
    try:
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False


# Проверка числа
# number = 35742549198872617291353508656626642567
# number = 2147483647
number = 11111111111111111111111

start_time = time.time()
result = is_prime(number)
end_time = time.time()

print(f"Число {number} {'простое' if result else 'составное'}")
print(f"Время выполнения (с обработкой исключений): {end_time - start_time} секунд")
