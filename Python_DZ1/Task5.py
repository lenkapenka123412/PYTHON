"""Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых 
трех цифр равна сумме последних трех.

Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

Вам требуется написать программу, которая проверяет счастливость билета 
с номером n и выводит на экран yes или no."""

# n = int(input("Введите число: "))

# x = n // 1000
# y = n % 1000

# summ1 = (x//100)+(x//10%10)+(x%10)
# summ2 = (y//100)+(y//10%10)+(y%10)

# print(summ1)
# print(summ2)

# if summ1 == summ2:
#     print("yes")
# else:
#     print("no")

n = 385916
x1 = n//100000
x2 = n//10000%10
x3 = n//1000%10
x4 = n//100%10
x5 = n//10%10
x6 = n%10
if (x1+x2+x3) == (x4+x5+x6):
    print("Yes")
else:
    print("no")
