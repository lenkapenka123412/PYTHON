# import random
# n = int(input('Введите количество элементов первой последовательности: '))
# first = []
# for _ in range(n):
#     first.append(random.randint(1, 10))

# m = int(input('Введите количество элементов первой последовательности: '))
# second = []
# for _ in range(m):
#     second.append(random.randint(1, 10))
# print(first)
# print(second)
# for i in range(n):
#     if first[i] not in second:
#         print(first[i], end = " ")


# import random
# n = int(input('Введите количество элементов: '))
# a = []
# count = 0
# for i in range(n):
#     a.append(random.randint(1, 10))
# print(a)
# for i in range(1,n-1):
#     if a[i - 1] < a[i] > a[i + 1]:
#         count += 1
#         print(f'Элемент {a[i]} на позиции {i+1}')
# print(f'Количество элементов: {count}')