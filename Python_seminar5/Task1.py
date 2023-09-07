# ['яблоко', '...'], 'grape': 'виноград'}

#str, int, float, bool, tuple, frozenset

# some_str = 'привет'

# print(id(some_str))

# some_str += '!'

# print(id(some_str))

# print(some_dict['apple'][1])

# some_dict['orange'] = 'апельсин'

# print(some_dict)

#

# for el in some_dict:

# print(el, some_dict[el])

#

# for value in some_dict.values():

# print(value)

# text = input('Введите слово: ') # OUI
# dictionary1 = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U':'1', 'L':'1', 'N':'1', 'S':'1', 'T':'1', 'R':'1', 'D':'2', 'G':'2', 'B':'3', 'C':'3', 'M':'3', 'P':'3', 'F':'4'}
# dict2 = {'H':'4', 'V':'4', 'W':'4', 'Y':'4', 'K':'5', 'J':'8', 'X':'8', 'Q':'10', 'Z':'10', 'А':'1', 'В':'1'}

# summ = 0
# for i in text:
# summ = summ + dictionary1.get(i.upper(), 0) + dict2.get(i.upper(), 0)
# print(summ)

# # dict = {frozenset(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']) : 1}
# # for i in text:
# # for key in dictionary1:
# # if i in key:
# # summa += dictionary1[key]

# # erudit = {'AEIOULNSTR': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 4, 'K': 5, 'JX': 8, 'QZ':10,
# # 'АВЕИНОРСТ': 1, 'ДКЛМПУ': 2, 'БГЁЬЯ': 3, 'ЙЫ': 4, 'ЖЗХЦЧ': 5, 'ШЭЮ': 8, 'ФЩЪ': 10}

# some_dict = {}

# some_str = 'aabc'
# for s in some_str:
# if s in some_dict:
# some_dict[s] = some_dict[s] + 1
# else:
# some_dict[s] = 1

""""Задача №31. Общее обсуждение
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0
= 0, a1
= 1, ak
= ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию"""

# def fib(N):
#     if N == 0:
#         return 0
#     elif N == 1:
#         return 1
#     else:
#         fib(N - 1) + fib(N - 2)

####################################################

# def factorial_recursive(n): # 5 -> 5 * 4 * 3 * 2 * 1
# if n == 1:
# return n
# else:
# return n * factorial_recursive(n - 1)

# def fact(n):
# mult = 1
# for i in range(2, n + 1):
# mult *= i
# return mult

# import time
# n = 30

# start = time.perf_counter()
# print(factorial_recursive(n))
# end = time.perf_counter()
# duration_1 = end - start

# start = time.perf_counter()
# print(fact(n))
# end = time.perf_counter()
# duration_2 = end - start

# print(duration_1 / duration_2)

##########################################

"""Задача №33. Общее обсуждение
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""

#############################################

# def replace_grades(grades):
#     max_grade = max(grades)
#     min_grade = min(grades)
#     replaced_grades = [min_grade if grade == max_grade else max_grade for grade in grades]
#     return replaced_grades

# input_grades = input("Введите оценки, разделенные пробелами: ")
# grades_list = list(map(int, input_grades.split()))

# replaced_grades_list = replace_grades(grades_list)
# replaced_grades = ' '.join(map(str, replaced_grades_list))

# print("Output:", replaced_grades)

#####################################

# import random
# def zamena(ocenka):
# min = ocenka[0]
# max = ocenka[0]
# for i in range(len(ocenka)):
# if ocenka[i] > max:
# max = ocenka[i]
# elif ocenka[i] < min:
# min = ocenka[i]
# for j in range(len(ocenka)):
# if ocenka[j] == max:
# ocenka[j] = min
# return(ocenka)

# n = int(input('Введите число: '))
# ocenka = []
# for _ in range(n):
# ocenka.append(random.randint(1, 5))
# print(ocenka)
# print(zamena(ocenka))

####################################

"""Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes """

##################################

# def isSimply(N):
#     i = 2
#     while i < N:
#         if N % i == 0:
#             return False
#         i += 1
#         return True

# for i in range(100):
#     if isSimply(i):
#         print(i)

#####################################

# def isSimply(N):
#     i = 2
#     while i < N:
#         if N % i == 0:
#             return False
#         i += 1
#         return True

# for i in range(100):
#     if isSimply(i):
#         print(i)

# n = int(input())
# for i in range(2, n // 2 + 1):
#     if n % i == 0:
#         print('NO')
#         break
# else:
#     print('YES')

# def print_reverse_sequence():
#     number = int(input("Введите количество элементов: "))
#     if number > 0:
#         element = int(input("Введите элемент: "))
#         print_reverse_sequence()
#         print(element, end=" ")

# print_reverse_sequence()