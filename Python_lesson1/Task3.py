"""В некоторой школе решили набрать три новых математических класса и оборудовать 
кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. 
Известно количество учащихся в каждом из трех классов. Выведите наименьшее 
число парт, которое нужно приобрести для них.
**Input:**
20
21
22
**Output:**
32"""

n = 20
m = 21
s = 22
x = ((n+1)//2 +(m+1)//2+(s+1)//2)
print(x)