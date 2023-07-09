"""4.Создайте список из случайных чисел. Найдите второй максимум.

a = [1, 2, 3] # Первый максимум == 3, второй == 2"""
import random

def find_second_maximum(numbers):
    if len(numbers) < 2:
        return None

    # Базовый случай рекурсии
    if len(numbers) == 2:
        return min(numbers[0], numbers[1])

    # Разделение списка на две половины
    middle = len(numbers) // 2
    left_half = numbers[:middle]
    right_half = numbers[middle:]

    # Рекурсивный вызов для левой и правой половин
    left_max = find_second_maximum(left_half)
    right_max = find_second_maximum(right_half)

    # Нахождение второго максимума среди левого и правого максимумов
    if left_max is None:
        return right_max
    elif right_max is None:
        return left_max
    else:
        return max(left_max, right_max)

# Создание списка случайных чисел
n = int(input("Введите количество элементов списка: "))
numbers = [random.randint(1, 100) for _ in range(n)]
print("Список чисел:", numbers)

# Поиск второго максимума
second_maximum = find_second_maximum(numbers)

# Вывод результата
if second_maximum is None:
    print("В списке недостаточно элементов.")
else:
    print("Второй максимум:", second_maximum)