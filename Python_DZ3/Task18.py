"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент 
к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество 
элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X

*Пример:*
5
    1 2 3 4 5
    6
    -> 5
"""


def find_closest_element(A, X):
    closest_element = A[0]
    min_difference = abs(X - A[0])

    for num in A:
        difference = abs(X - num)
        if difference < min_difference:
            min_difference = difference
            closest_element = num

    return closest_element

# Ввод данных
N = int(input("Введите количество элементов в массиве: "))
A = list(map(int, input("Введите элементы массива через пробел: ").split()))
X = int(input("Введите число X: "))

# Поиск ближайшего элемента
closest = find_closest_element(A, X)

# Вывод результата
print("Самый близкий по величине элемент к числу X:", closest)