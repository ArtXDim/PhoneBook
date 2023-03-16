import view
import model

def run():
    view.greetings()
    while True:
        view.menu()
        answer = input('Ответ:')
        if answer == '1':
            model.read_phonebook()
        elif answer == '2':
            model.add_contact()
        elif answer == '3':
            model.search_contact(input("Найти:"))
        elif answer == '4':
            model.change_contact(input("Изменить контакт:"))
        elif answer == '5':
            model.delete_contact(input("Удалить контакт:"))        
        elif answer == '6':
            break

