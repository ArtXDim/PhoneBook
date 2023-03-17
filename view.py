def  greetings (): 
    print ( '**ТЕЛЕФОННАЯ КНИГА**' ) 
    
    
def  menu (): 
    my_list = ['1 - Показать контакт', 
              '2 - Добавить контакт', 
              "3 - Найти контакт", 
              '4 - Изменить контакт',  
              '5 - Удалить контакт', 
              '6 - Закрыть книгу'] 
    print('\n'.join(my_list))   


def print_add():
    print("Контакт успешно добавлен!")


def print_search():
    print('Данного контакта нет в вашем справочнике\n')
    print('Xотите добавить отсутствующий контакт? ')
    add = str(input("да/нет? :  ")).lower()


def print_contacts(contacts):
    if not contacts:
        print("Список контактов пуст.")
    else:
        print("Список контактов:")
        for contact in contacts:
            print(f"{contact['name']}: {contact['phone']}")


def print_error(message):
    print(f"Ошибка: {message}")

print(menu())
print(print_search())