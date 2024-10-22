import time
from concurrent.futures import ThreadPoolExecutor
import math
import numpy as np


# Функция для вычисления факториала в одном потоке
def factorial_single_thread(n):
    return math.factorial(n)


# Функция для вычисления факториала в нескольких потоках
def factorial_multi_thread(n, num_threads):
    # Разделяем диапазон на части
    ranges = np.array_split(np.arange(1, n + 1), num_threads)

    def partial_factorial(r):
        result = 1
        for i in r:
            result *= i
        return result

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(partial_factorial, ranges))

    # Перемножаем результаты всех потоков
    final_result = 1
    for res in results:
        final_result *= res

    return final_result


# Основная функция для сравнения времени выполнения
def compare_factorials(n):
    # Однопоточный расчет
    start_time = time.time()
    result_single = factorial_single_thread(n)
    time_single = time.time() - start_time

    print(f"Однопоточный расчет: {time_single:.4f} секунд")

    # Многопоточные расчеты с 2, 4 и 8 потоками
    for num_threads in [2, 4, 8]:
        start_time = time.time()
        result_multi = factorial_multi_thread(n, num_threads)
        time_multi = time.time() - start_time

        assert (
            result_single == result_multi
        ), f"Результаты не совпадают для {num_threads} потоков!"
        print(f"{num_threads}-поточный расчет: {time_multi:.4f} секунд")


if __name__ == "__main__":
    n = 100000
    compare_factorials(n)
