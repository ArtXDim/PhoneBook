

def add_contact(surname , name, phone):
    with open ('phonenum.txt', 'a') as file:
        file.write(f"{Фамилия} {Имя} : {Телефон}\n")

# Для вывода все контактов
def show_contacts():
    with open ('phonenum.txt', 'r') as file:
        for line in file:
            print(line.strip())

# Для поиска контакта

def find_contact(surname):
    with open ('phonenum.txt', 'r') as file:
        for line in file:
            if surname in line or name in line:
                return line.strip()
            return 'Контакт не найден'
