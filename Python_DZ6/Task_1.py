"""Напишите функцию f, которая на вход принимает два числа a и b, и возводит 
число a в целую степень b с помощью рекурсии.

Функция не должна ничего выводить, только возвращать значение.

Пример:

a = 3; b = 5 -> 243 (3⁵)
a = 2; b = 3 -> 8 """


# def f(a, b):
#     if b == 0:
#         return 1
#     elif b < 0:
#         return 1 // f(a, -b)
#     else:
#         return a * f(a, b - 1)

# a = 3
# b = 5
# print(f(a, b))

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# Функция не должна ничего выводить, только возвращать значение.
# sum(2, 2)
# 4

def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum(a-1, b+1)

# Пример использования
a = 2
b = 2
result = sum(a, b)
print(sum(a, b))