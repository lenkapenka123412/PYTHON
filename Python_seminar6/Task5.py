"""Задача No43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару, 
которую необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках.
Ввод: Вывод:
1232 3 2
15 минут"""

def count_equal_pairs(numbers):
    count = 0
    frequency = {}
    for num in numbers:
        if num in frequency:
            count += frequency[num]
            frequency[num] += 1
        else:
            frequency[num] = 1
    return count

# Ввод списка чисел
numbers = []
print("Введите список чисел, каждое число на новой строке. Для завершения ввода введите пустую строку.")
while True:
    num = input()
    if num == "":
        break
    numbers.append(int(num))

# Подсчет пар равных элементов
result = count_equal_pairs(numbers)

# Вывод результата
print("Количество пар элементов, равных друг другу:", result)