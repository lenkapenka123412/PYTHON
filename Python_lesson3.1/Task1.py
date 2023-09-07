# пример кода функции

# def seyHello():
#     print('Hello')
#     print('world')
#     print('and everybody')

# seyHello()

###################################

# def square(x):
#     print('Квадрат числа ', x, '=', x**2 )

# square(5)

####################################

# def square(x):
#     print('Квадрат числа ', x, '=', x**2 )

# n = int(input('Введите число: '))
# square(n)

########################################

# def square(x):
#     print('Квадрат числа ', x, '=', x**2 )

# for i in range(1,11):
#     square(i)

#######################################

# def square(x, y):
#     print(x*y)

# square(5, 2)

#########################################

# def even(a):
#     if a%2 == 0:
#         print(a, 'Четное')
#     else:
#         print(a, 'Не четное')

# # n = int(input('Введите число: '))
# # even(n)

# for i in range(20, 30):
#     even(i)

###########################################

# def factorial(n):
#     pr = 1
#     for i in range(2, n+1):
#         pr = pr*i
#     print(pr)

# factorial(5)

##############################################

# if 5>1:
#     def primer():
#         print('hello')
# else:
#     def primer():
#         print('HELLO')
# primer()

###########################################

# n = abs(-7)
# print(n)

###############################

# m = max(1,2,3,4,5,6)
# print(m)

######################
# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)
# print(fib(8))

####################################

'''Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
минимальные оценки на максимальные. Напишите программу, которая заменяет оценки 
Василия, но наоборот: все максимальные – на минимальные.'''


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

############################################

# from random import randint


# list_1 = [randint(1, 5) for item in range(1, 11)]
# print(list_1)
# list_sort = sorted(list_1)

# print(list_sort)
# min = list_sort[0]
# max = list_sort[-1]
# for i in range(len(list_1)):
#     if list_1[i] == max:
#         list_1[i] = min
# print(list_1)

#######################################

# list=[1,2,3,5,4,4,1]
# for i in range(1,7):
#     if list[i]==5:
#         list[i]=1
#     if list[i]==4:
#         list[i]=2
# print(list)

################################

# from random import randint
# print(list_1 := [randint(1, 5) for _ in range(10)])

# max1 = max(list_1)
# print(max1)
# for i in range(len(list_1)):
#     if max1 == list_1[i]:
#         list_1[i] = 1

# print(list_1)

##########################################

'''1. Напишите функцию, которая принимает одно 
число и проверяет, является ли оно простым

*Напоминание: Простое число - это число, 
которое имеет 2 делителя: 1  и n(само число)*'''

# nam1 = int(input("Введите число: "))

# def isPrime(nam1):
#     for num in range(2, nam1 // 2 + 1):
#         if nam1 % num == 0:
#             return "Число сложное!"
#     return "Число простое!"

# print(isPrime(nam1))

##########################################

'''Задача №37. Решение в группах
15 минут
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3'''





