# В этом файле методы для вывода информации.
import re

# Для вывода 'все-все в своих строках'.
def all_string_output ():
    whole_pb = get_pb_list()
    for i in range(len(whole_pb)):
        for j in range(len(whole_pb[i])):
            print(whole_pb[i][j])
        print()

# Для вывода всего контакта в строке.
def person_output():
    whole_pb = get_pb_list()
    for person in whole_pb:
        print(' '.join(person))

# Для получения информации из файла с контактами.
def get_pb_list():
    phonebook_list = []
    with open('phonebook.txt', 'r', encoding = 'utf-8') as pb:
        for line in pb:
            line = line[0:len(line)-1]
            line_lst = re.split(" - | ", line)
            phonebook_list.append(line_lst)
    return phonebook_list

# Выбор типа отображения.
def switch_outtype():
    outtype = input('Выберите тип отображения:\n1 - Все в своей строке\n2 - Каждый контакт в своей строке\n ')
    all_string_output() if outtype == '1' else person_output()
