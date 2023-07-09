# Вводится колличество чисел, затем чамми числа, найти сумму четных числе.

count = int(input('Введите колличество чисел: '))
summa = 0
for _ in range(count):
    namber = int(input("Введите число: "))
    if namber % 2 == 0:
        summa += namber
print(summa)
