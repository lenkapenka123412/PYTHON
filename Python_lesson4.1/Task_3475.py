"""За день машина проезжает n
 километров. Сколько дней нужно, чтобы проехать маршрут длиной m
 километров?

Входные данные
Программа получает на вход числа n
 и m
 (целые, положительные).

Выходные данные
Выведите ответ на задачу."""

import math
n = int(input("ВВедите расстояние: "))
m = int(input("ВВедите маршрут: "))
x = math.ceil(m/n)
print(x)