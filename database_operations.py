# В этом файле описываются методы для работы с базой данных: для добавления, удаления, редактирования записей.

def append_position ():
    lst_pos = input('Введите имя, фамилию, номер телефона и комментарий к нему через пробел ').split()
    with open('telephone_info.txt', 'a', encoding = 'utf-8') as phonebook:
        phonebook.writelines(f'{lst_pos[0].upper()} - {lst_pos[1].upper()} - {lst_pos[2]} - {lst_pos[3].upper()}\n')

def get_position ():
    pos_to_find = input('введите информацию для поиска: ').upper()
    with open('telephone_info.txt', 'r', encoding = 'utf-8') as phonebook:
        for line in phonebook:
            if pos_to_find in line:
                print(line)


