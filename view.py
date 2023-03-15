fields_names = ['id', 'Имя', 'Фамилия', 'Телефон']


def greetings():
    print('**ТЕЛЕФОННАЯ КНИГА**')
    
# сообщения

greetings = "Здравствуйте. Это Ваша телефонная книга"
error = 'Ошибка. Проверьте  введенные данные'
enter = 'Добавьте контакт'
success_add = 'Контакт добавлен'
success_save = 'Данные сохранены'
bye = 'До свидания'

def menu():
    print("1 - Показать контакты")
    print("2 - Добавить контакт")
    print("3 - Найти контакт")
    print("4 - Сохранить контакт")
    print("5 - Удалить контакт")
    print("6 - Закрыть книгу")


# словарь ответов
'1': 'show'
'2': 'add'
'3': 'find'
'4': 'save'
'5': 'delet'
'6': 'exit'

def find():
    return None


file_name = 'phonenum.txt'
