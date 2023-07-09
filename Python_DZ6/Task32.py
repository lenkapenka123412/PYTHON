""" Задача 32: Определить индексы элементов массива (списка), значения которых 
принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
"""

def find_indexes_in_range(arr, minimum, maximum):
    indexes = [index for index, value in enumerate(arr) if minimum <= value <= maximum]
    return indexes

# Пример использования функции
arr = [2, 5, 8, 3, 9, 7, 1, 6]
minimum = 3
maximum = 7

result = find_indexes_in_range(arr, minimum, maximum)
print("Индексы элементов, принадлежащих заданному диапазону:")
print(result)