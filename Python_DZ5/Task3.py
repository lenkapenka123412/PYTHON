# 3.Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.

import random

def find_max_occurrences(numbers):
    occurrences = {}

    for num in numbers:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1

    max_occurrences = max(occurrences.values())

    return max_occurrences

# Создание списка случайных чисел
n = int(input("Введите количество элементов списка: "))
numbers = [random.randint(1, 10) for _ in range(n)]
print("Список чисел:", numbers)

# Поиск максимального количества повторений
max_occurrences = find_max_occurrences(numbers)

# Вывод результата
print("Максимальное количество повторений:", max_occurrences)