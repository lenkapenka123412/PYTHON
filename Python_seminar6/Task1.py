## подсказка для решения задачи со сбоором ягод с кусов
# arr_count = list()
# for i in range(len(arr) - 1):
#      arr_count.append(arr[-2] + arr[-1] + arr[0])
# print(max(arr_count))

"""Задача No39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, 
в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит число N - 
количество элементов в первом массиве, затем N чисел - элементы массива. 
Затем число M - количество элементов во втором массиве. 
Затем элементы второго массива
Ввод:
7
3 1 3 4 2 4 12
6
4 15 43 1 15 1
Вывод:
3 3 2 12
(каждое число вводится с новой строки)
"""
def find_unique_elements():
    # Ввод первого массива
    n = int(input("Введите количество элементов первого массива: "))
    array1 = set(input("Введите элементы первого массива через пробел: ").split())

    # Ввод второго массива
    m = int(input("Введите количество элементов второго массива: "))
    array2 = set(input("Введите элементы второго массива через пробел: ").split())

    # Поиск уникальных элементов
    unique_elements = [element for element in array1 if element not in array2]

    # Вывод результатов
    print("Уникальные элементы первого массива, которых нет во втором массиве:")
    print(*unique_elements)

find_unique_elements()
