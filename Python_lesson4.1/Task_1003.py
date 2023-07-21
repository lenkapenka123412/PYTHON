"""Однажды, посетив магазин канцелярских товаров, Вася купил X карандашей, Y ручек и Z фломастеров. 
Известно, что цена ручки на 2 рубля больше цены карандаша и на 7 рублей меньше цены фломастера. 
Также известно, что стоимость карандаша составляет 3 рубля. 
Требуется определить общую стоимость покупки.

Входные данные
В единственной строке входного файла INPUT.TXT записаны три натуральных 
числа X, Y и Z через пробел, каждое из которых не превышает 109.

Выходные данные
В выходной файл OUTPUT.TXT выведите одно целое число – стоимость покупки в рублях."""

x, y, z = map(int, input("ведите 3 числа через пробел: ").split()) # карандаш

x1 = 3
y1 = x1 + 2
z1 = y1 + 7

print((x*x1) + (y*y1) + (z*z1))