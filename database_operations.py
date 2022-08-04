# В этом файле описываются методы для работы с базой данных: для добавления, удаления, редактирования записей.
import re
# Добавить контакт в справочник. РАБОТАЕТ
def append_position ():
    lst_pos = input('Введите имя, фамилию, номер телефона и комментарий к нему через пробел ').split()
    with open('phonebook.txt', 'a', encoding = 'utf-8') as phonebook:
        phonebook.writelines(f'{lst_pos[0]} {lst_pos[1]} - {lst_pos[2]} - {lst_pos[3]}\n')
    print('Контакт добавлен.')

# Найти контакт(ы) в справочнике. 
def get_position ():
    request_lst = []
    pos_to_find = input('Введите имя, фамилию или номер телефона для поиска: ').upper().split()
    with open('phonebook.txt', 'r', encoding = 'utf-8') as phonebook:
        for line in phonebook:
            if (pos_to_find[0] or pos_to_find[1] or pos_to_find[2]) in line.upper():
                request_lst.append(line[:len(line)-1])
    return request_lst

# Изменить контакт. 
def rewrite_person ():
    rewrite_req = []
    while len(rewrite_req) == 0:
        rewrite_req = get_position()
    if len(rewrite_req) > 1:
        print('Найдены следующие контакты:')
        for i in range(len(rewrite_req)):
            print(f'{i+1} - {rewrite_req[i]}')
        req_person = int(input('Укажите номер контакта, который хотите изменить: '))
        rewrite_req = rewrite_req[req_person]
    rewrite_list = rewrite_req[0].split()
    req_position = int(input('1 - Имя\n2 - Фамилия\n3 - Номер телефона\n4 - Комментарий\nЧто хотите изменить? '))
    rewritin_part = input('Введите новое значение: ')
    pbread = open('phonebook.txt', 'r', encoding = 'utf-8')
    data = pbread.read()
    data = data.split('\n')
    for i in range(len(data)):
        if (rewrite_list[0] and rewrite_list[1] and rewrite_list[2] and rewrite_list[3]) in data[i]:
            data[i] = data[i].replace(rewrite_list[req_position-1], rewritin_part)
    pbread.close()
    pbwrite = open('phonebook.txt', 'w', encoding = 'utf-8')
    for i in range(len(data)):
        pbwrite.write(str(f'{data[i]}\n'))
    pbwrite.close()
    print('Контакт изменен.')

    # Удалить контакт. 
def delete_person ():
    delete_req = []
    while len(delete_req) == 0:
        delete_req = get_position() # Запрос данных контакта, по которым что-то можно найти.
    if len(delete_req) > 1:
        print('Найдены следующие контакты:')
        for i in range(len(delete_req)):
            print(f'{i+1} - {delete_req[i]}')
        del_person = int(input('Укажите номер контакта, который хотите удалить: '))
        # delete_req = re.split(" - | ", delete_req[del_person-1])
        for i in range(len(delete_req)):
            if delete_req[i] != delete_req[del_person-1]:
                delete_req.remove(delete_req[del_person])
    wanna_delete = input(f' Найден контакт {delete_req}.\n Действительно хотите его удалить? Д / Н ').lower()
    if wanna_delete == 'д':
        pbread = open('phonebook.txt', 'r', encoding = 'utf-8')
        data = pbread.read()
        data = data.split('\n')
        for i in range(len(data)):
            if (delete_req[0][:len(delete_req[0])-1]) in data[i]:
                data[i] = ''
        pbread.close()
        pbwrite = open('phonebook.txt', 'w', encoding = 'utf-8')
        for i in range(len(data)):
            pbwrite.write(str(f'{data[i]}\n'))
        pbwrite.close()
        pbread = open('phonebook.txt', 'r', encoding = 'utf-8')
        data = pbread.read().split('\n')
        pbread.close()
        pbwrite = open('phonebook.txt', 'w', encoding = 'utf-8')
        for i in range(len(data)):
            if data[i] != "":
                pbwrite.write(str(f'{data[i]}\n'))
    print('Контакт удален.')
