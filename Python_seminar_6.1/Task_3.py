"""Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод: Вывод:
1 2 3 2 3 2"""

from random import randint

namber1 = int(input("Введиче кол-во эл 1 списка: "))
list_1 = [randint(0,10) for i in range(namber1)]

print(list_1)

dic = {}
for i in list_1:
    value = dic.get(i, 0) + 1
    dic[i] = value
print(dic)

count = 0

for i in range(11):
    count += dic.get(i, 0) // 2 
print(count)






