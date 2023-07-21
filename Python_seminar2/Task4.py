# n = int(input())
# s = 0
# s1 = 1
# s2 = 1
# while s1 < n or s2 < n:
#     s1 = s1 + s2
#     s2 = s1 + s2
#     s += 2
# if s1 == n:
#     s = s + 1
# if n + s1 == s2 or n + s2 == s1 or s1 == n:
#     print(s)
# else:
#     print(-1)

number = int(input('Введите число: '))

fibo_prev = 0
fibo_cur = 1
index = 1

while fibo_cur < number:
    fibo_prev, fibo_cur = fibo_cur, fibo_prev + fibo_cur
    index += 1
if fibo_cur == number:
    print(f'Число {number} идет {index} числом в последовательности Фибоначчи')
else:
    print(-1)
