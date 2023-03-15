

def add_contact():
    surname = input('Введите фамилию:')
    name = input('Введите имя:')
    phone = input('Введите телефон :')
    with open ('phonenum.txt', 'a', encoding='utf-8') as file:
        file.write(surname + ' '+ name +'   :' + phone ' ' +'\'n')
        

# Для вывода всеx контактов
def show_contacts():
    with open ('phonenum.txt', 'r', encoding = "utf-8") as file:
        for line in file:
            print(line.strip())

# Для поиска контакта

def find_contact(surname):
    with open ('phonenum.txt', 'r', encoding = "utf-8") as file:
        for line in file:
            if surname in line or name in line:
                return line.strip()
            return 'Контакт не найден'
