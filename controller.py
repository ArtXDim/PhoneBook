import view
import model

def run():
    veiw.greatings()
    while true:
        view.menu()
        answer = input('Ответ')
        if answer == '1':
            data = model.read_phonebook()
            view.show_phonebook()
        elif answer == '2':
            model.add_contact()
        elif answer == '3':
            model.find()
        elif answer == '4':
            break

