# Функции

# Зачада - определние суммы элементов от 1 до n c помощью функции; 

# def sum_nambers(n): # создали функцию
#     summa = 0 # создали переменную куда будем класть нашу сумму
#     for i in range(1, n+1): # запускаем счетчик для подсчитываания суммы от 1 до n
#         summa += i # после каждой итерации увенличиваем аншу сумму на i
#     print(summa) # печать суммы
# sum_nambers(5) # вызов переменной


# # Зачада - второй вариант - определние суммы элементов от 1 до n c помощью функции; 

# def sum_nambers(n): # создали функцию
#     summa = 0 # создали переменную куда будем класть нашу сумму
#     for i in range(1, n+1): # запускаем счетчик для подсчитываания суммы от 1 до n
#         summa += i # после каждой итерации увенличиваем аншу сумму на i
#     return summa # оператор ретерн. Оператор return завершает работу функции
# print(sum_nambers(5)) # вызов переменной/ вызываем функцию и сразу же выводим результаты нашей функции

# Зачада - третий вариант - определние суммы элементов от 1 до n c помощью функции; 

# def sum_nambers(n): # создали функцию
#     summa = 0 # создали переменную куда будем класть нашу сумму
#     for i in range(1, n+1): # запускаем счетчик для подсчитываания суммы от 1 до n
#         summa += i # после каждой итерации увенличиваем аншу сумму на i
#     return summa # оператор ретерн. Оператор return завершает работу функции
# a = sum_nambers(5)
# print(a) # выводим перемнную а

# def sum_str(*args): # функция, которая может принимать неограниченное количество аргументов.
#     res = " " # создали переменную res которая имеет тип данных «строка»
#     for i in args: # проходимся по всем элементам нашей переменной args
#         res += i # при каждой итерации мы к переменной res будем добавлять нашу перемнную i и затем её вернум
#     return res # возвращаем нашу перменную res
# print(sum_str('q', 'e', 'l'))