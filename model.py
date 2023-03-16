def read_phonebook():
    with open('books.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
    input("\nНажмите любую клавишу для продолжения...\n")


def search_contact(name):
    print('Hайден(ы) контакт(ы) : ')
    with open('books.txt', 'r', encoding='utf-8') as file:
        s = file.readlines()
    count = 0
    for i in s:
        if name in i:
            print(i, sep="\n")
            count += 1
    if count == 0:
        print('Данного контакта нет в вашем справочнике\n')
        print('Xотите добавить отсутствующий контакт? ')
        add = [(input("да/нет? :  ")).lower()]
        if 'да' in add:
            add_contact()
    input("нажмите любую клавишу для продолжения...")


def add_contact():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер: ')
    with open('books.txt', 'a+', encoding='utf-8') as file:
        file.write('%s\n'% (last_name + ' ' + first_name + ' ' + phone_number))
    print(f'контакт {last_name} добавлен.\n ')


def change_contact(name):
    if len(name) == 0:
        print("Данные не введены")
        return
    with open('books.txt', 'r', encoding='utf-8') as file:
        s = file.readlines()
        for i in range(0, len(s)):
            if name in s[i]:
                s[i] = input("Введите новые данные: ") + "\n"             
    non_empty_lines = (i for i in s if not i.isspace())
    with open('books.txt', 'w', encoding='utf-8') as file_1:
        file_1.writelines(i for i in non_empty_lines)      


def delete_contact(name):
    with open('books.txt', 'r+', encoding='utf-8') as file:
        s = file.readlines()
        for i in range(0, len(s)-1):
            if name in s[i]:
                s.pop(i)
    with open('books.txt', 'w', encoding='utf-8') as file_1:
        file_1.writelines(i for i in s)
