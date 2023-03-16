def read_phonebook():
    with open('books.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
      

def search_contact(name):
    with open('books.txt', 'r', encoding='utf-8') as file:
        files = [i for i in file.readline()]
        for i in files:
            if name in i:
                print(i)
            else:
                print('хотите добавить отсутствующий контакт? ')
                add = (input("да/нет? :  ")).lower
                if add == 'да':
                    add_contact()
                else:
                    print('---')
                    return
    print('выход в главное меню...')

def add_contact():
    first_name = input('введите имя: ')
    last_name = input('введите фамилию: ')
    phone_mnumber = input('введите номер: ')
    with open('books.txt', 'a', encoding='utf-8') as file:
        file.write(first_name + ' ' + last_name + ' ' + phone_mnumber + '\n')
        print(" ")
        print(f'контакт {first_name} добавлен. ')

