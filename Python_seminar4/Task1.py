# добавление элементов в список
# import random
# some_list = []
# count = int(input('Кол-во элементов: '))
# for _ in range(count):
#     number = random.randint(1, 10)
#     some_list.append(number)
# print(some_list)

# ---------------
# some_list = [1, 'hello', True, 5.43, [1, 2, 3], {1, 2, 3}]

# for el in some_list:
#     print(el)

# for letter in 'hello':
#     print(letter)

# for ind in range(len(some_list) - 1, -1, -1):  # 6, 5, 4, 3, 2, 1
#     print(some_list[ind], ind)

# print(type(some_list))

# Вводится сначала кол-во чисел, затем сами числа, добавить их в список

# some_list = [1, 2, 3, 4, 5]
# print(some_list[::-1])

#- ----------------

# some_list = [1, 2, 3, 4, 5]
# print(some_list[::-1])
# some_list[0] = '1'
# some_tuple = tuple(some_list)
# some_tuple[0] = '1'
# new_list = list(some_tuple)

# -----------------
# import random
# import time
# some_set = set()
# for _ in range(10 ** 6):
#     number = random.randint(1, 10 ** 6)
#     some_set.add(number)

# some_list = list(some_set)

# start = time.perf_counter()
# print(-1 in some_list)
# end = time.perf_counter()
# list_duration = end - start


# start = time.perf_counter()
# print(-1 in some_set)
# end = time.perf_counter()
# set_duration = end - start
# print(list_duration / set_duration)

#-------
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# some_list = []
# count = int(input('Введите кол-во чисел: '))
# for _ in range(count):
#     some_list.append(int(input()))

# res_count = 0
# for ind in range(0, count - 1):
#     if some_list[ind] < some_list[ind + 1]:
#         res_count += 1
# print(res_count)

#------
'''Напишите программу, которая принимает на вход
строку, и выводит количество повторов каждого символа
Input: aaabcaadcdd
Output: a: 5, b: 1, c: 2, d: 3'''

#----------------

# some_str = input()
# for letter in set(some_str):  # a
#     count = 0
#     for letter_1 in some_str:
#         if letter == letter_1:
#             count += 1
#     print(f"{letter}: {count}", end=' ')

# some_str = input()
# for letter in set(some_str):
#     print(f"{letter}: {some_str.count(letter)}", end=' ')

# # Последовательность ФИБОНАЧИИ

# def f(n):
#     if n in [1,2]: # базис для завершения рекурсии.
#         return 1
#     return f(n-1) + f(n-2)
# list_1 = []

# for i in range(1, 10):
#     list_1.append(f(i))
# print(list_1)

# # Бинарный поиск или алгорим быстрой сортировки

def qick_sort(array): # создаем новый массив
     if len(array) <= 1: # если длинна массива меньше или равно 1(указали базис рекурсии)
         return array 
     else:
         pivor = array[0] # сохраняем первый элементв переменную pivor
     less = [i for i in array[1:] if i <= pivor] 
     less1 = [i for i in array[1:] if i > pivor]
     return qick_sort(less) + [pivor] + qick_sort(less1)

print(qick_sort([14,2,5,56,4,5,8,3,25,3,2,3,5,5,2,5,52]))



