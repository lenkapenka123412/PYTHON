# Задача 16
# N = int(input("Введите количество элементов в массиве: "))
# A = []
# for i in range(N):
#    A.append(int(input()))

# X = int(input("Введите число X: "))

# Перебираем все элементы массива A и считаем, сколько раз встречается число X
# count = 0
# for i in range(N):
#     if A[i] == X:
#         count += 1

# print(count)


# Задача 18
# N = int(input("Введите количество элементов в массиве: "))
# A = []
# for i in range(N):
#     A.append(int(input()))

# X = int(input("Введите число X: "))

# Выбираем первый элемент массива A как наименьшую разность
# min_diff = abs(A[0] - X)
# closest = A[0]

# Перебираем все элементы массива A и выбираем элемент с наименьшей разностью
# for i in range(N):
#    if abs(A[i] - X) < min_diff:
#        min_diff = abs(A[i] - X)
#        closest = A[i]

# print(closest)

# word = input("Введите слово: ")

# Словарь с оценками для каждой буквы
# values = {
#    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1,
#    "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1,
#    "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
# }

# Подсчитываем стоимость слова
# score = 0
# for letter in word:
#    score += values[letter.upper()]

# print("Стоимость слова:", score)

# input_string = input("Введите строку: ")
# counts = {}

# Подсчитываем количество повторений каждого символа
# for char in input_string.split():
#     if char in counts:
#         counts[char] += 1
#     else:
#         counts[char] = 1

# Создаем новую строку с постфиксами _n
# output_string = ""
# for char in input_string.split():
#     if counts[char] < 1:
#         output_string += char + "_" + str(counts[char] - 1) + " "
#         counts[char] -= 1
#     else:
#         output_string += char + " "

# print("Output:", output_string)

# Задача 27
input_string = input("Введите строку: ")
words = set(input_string.split())

print("Количество различных слов:", len(words))
