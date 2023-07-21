# def f(x):
#     return x*x
# print(f(5))

##########################

# def f(x):
#      return x*x
# print(type(f))

############################

# def f(x):
#      return x*x
# a = f
# print(type(a))

#####################

# def calk1(a):
#     return a + a

# def calk1(a):
#     return a*a

# def math(op, x):
#     print(op(x))

# math(calk1, 5)

##########################

# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# calk1 = lambda a, b: a + b

# math(calk1, 5, 45)

##############################

# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# math(lambda a, b: a + b, 5, 45)

####################################

# Задача; В списке храняться числа. нужно выбрать только 
# четные и составить список пар: четные и их квадрат

# data = [1, 2, 3, 8, 65, 5, 6, 96, 7] 
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)

###############################

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 8, 65, 5, 6, 96, 7] 
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

###########################################

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)
# True 
# min = 2

# a=float(input())
# b=float(input())
# c=float(input())
# p=a+b+c
# print(p)

#####################

a,b,c = map(int, input("Введите числа: ").split())
print(a)
print(b)
print(c)