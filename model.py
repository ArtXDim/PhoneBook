def read_phonebook():
    with open('books.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
    input("нажмите любую клавишу для продолжения...")      

def search_contact(name):
    with open('books.txt', 'r', encoding='utf-8') as file:
        s = file.readlines()    
    count = 0   
    for i in s:
        if name in i:
            print('\n найден(ы) контакт(ы) : ')
            print(i)
            count += 1    
    if count == 0:                   
        print('хотите добавить отсутствующий контакт? ')
        add = [(input("да/нет? :  "))]
        if 'да' in add:
            add_contact() 
    input("нажмите любую клавишу для продолжения...")

def add_contact():
    last_name = input('введите фамилию: ')
    first_name = input('введите имя: ')
    phone_mnumber = input('введите номер: ')
    with open('books.txt', 'a+', encoding='utf-8') as file:
        file.write(last_name + ' ' + first_name + ' ' +  phone_mnumber + '\n')
    print(f'контакт {last_name} добавлен.\n ')
    input("нажмите любую клавишу для продолжения...")
