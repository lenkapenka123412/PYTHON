"""2.Создайте список из случайных чисел. Найдите номер его последнего локального максимума 
(локальный максимум — это элемент, который больше любого из своих соседей)."""

import random

def find_last_local_maximum(numbers):
    last_maximum_index = -1

    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
            last_maximum_index = i

    return last_maximum_index

# Создание списка случайных чисел
n = int(input("Введите количество элементов списка: "))
numbers = [random.randint(1, 100) for _ in range(n)]
print("Список чисел:", numbers)

# Поиск последнего локального максимума
last_maximum_index = find_last_local_maximum(numbers)

# Вывод результата
if last_maximum_index == -1:
    print("В списке нет локальных максимумов.")
else:
    print("Индекс последнего локального максимума:", last_maximum_index)