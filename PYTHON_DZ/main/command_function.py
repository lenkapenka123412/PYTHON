


# функция добавления контакта
def add_data():
    firstname = input('Введите имя: ')
    secondname = input('Введите фамилию: ')
    lastname = input('Введите фамилию: ')
    phonenumber = input('Введите телефон: ')
    while not phonenumber.isdigit():
        phonenumber = input('Введите номер телефона: ')
    str = f'{firstname} {secondname} {lastname} {phonenumber}\n'
    with open('main/new_example.txt', 'a', encoding='UTF-8') as data:
        data.write(str)

# функция поиска контакта
def find_data(str):
    with open('main/new_example.txt', 'r', encoding='UTF-8') as data:
        for line in data:
            if str.lower() in line.lower().split():
                print(line, end='\n')
    
# Функция удаления контакта
def del_data(str):
    with open('main/new_example.txt', 'r', encoding='UTF-8') as data:
        lst = data.readlines()
        print(lst)
        for line in range(len(lst)):
            if str.lower() in lst[line].lower().split():
                lst[line] = ''
        print(lst)
    with open('main/new_example.txt', 'w', encoding='UTF-8') as data:
        for i in lst:
            data.write(i)

# aункция вывода всех контактов
def full_list_data():
    with open('main/new_example.txt', 'r', encoding='UTF-8') as data:
        data = list(map(lambda x: x, data))
        print(data,'\n'.join(data))


# заменить контакт
# def edit_data(str):
    
    
    
    
   
    


    
    

                        
            
