"""
Задача №3745. Удаление символа
Дана строка. 'Bilbo.Baggins@bagend.hobbiton.shire.me' Удалите из этой строки все символы @."""

s = input("Введите строку: ")
print(s.replace('@', ''))