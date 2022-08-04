# Файл-диспетчер.
import database_operations as db
import info_output as io

def get_type ():
    output_type = int(input('Какой тип вывода предпочтителен:\n1 - Контакт в одной строке\n2 - Все в разных строках:\n '))
    return output_type
    
def get_request():
    request = int(input('Что хотите сделать?\n1 - Добавить контакт\n2 - Просмотреть контакт\n3 - Изменить контакт\n4 - Удалить контакт\n5 - Просмотреть весь справочник\n '))
    return request

def wanna_continue():
    global cont_intention
    cont_intention = True
    intent_code = input('Хотите продолжить? Д / Н\n ')
    cont_intention = True if intent_code == ('д' or 'Д') else False
    return cont_intention

def controller (request):
    match request:
        case 1:
            db.append_position()
        case 2:
            persons = db.get_position()
            for i in range(len(persons)):
                print(persons[i])
        case 3:
            db.rewrite_person()
        case 4:
            db.delete_person()
        case 5:
            io.switch_outtype()


    

