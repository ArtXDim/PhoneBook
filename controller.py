import view
import model

def run():
    view.greatings()
    while true:
        view.menu()
        answer = input('Ответ:')
        if answer == '1':
            data = model.read_phonebook()
            view.show_phonebook()
        elif answer == '2':
            model.add_contact()
        elif answer == '3':
            model.search_contact(input("Найти:"))
        elif answer == '4':
            model.change_contact()
        elif answer == '5':
            model.delete_contact()        
        elif answer == '6':
            break

