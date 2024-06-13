from tabulate import tabulate

def work_with_phonebook():
	
    choice = show_menu()

    phone_book = read_txt('phon.txt')

    
    while (choice != 7):

        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name=input('lastname: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('lastname: ')
            new_number = input('new  number: ')
            print(find_by_lastname_and_number(phone_book, last_name, new_number))  	
        elif choice == 4:
            lastname = input('lastname: ')
            print(delete_by_lastname(phone_book, lastname))
            write_txt('phon.txt', phone_book)
        elif choice == 5:
            number = input('number: ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            add_user(phone_book)
            write_txt('phon.txt', phone_book)


        choice=show_menu()


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Показать весь справочник\n"
          "2. Поиск абонента по фамилии\n"
          "3. Поиск абонента по фамилии и номеру телефона\n"
          "4. Удалить абонента из справочника и сохранить в текстовом формате\n"
          "5. Поиск абонента по номеру\n"
          "6. Добавить абонента в справочник и сохранить в текстовом формате\n"
          "7. Закончить работу")
    choice = int(input())
    return choice


def read_txt(filename): 

    phonebook=[]

    fields=['ФАМИЛИЯ', 'ИМЯ', 'ТЕЛЕФОН', 'ОПИСАНИЕ']

    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(', ')))
            phonebook.append(record)
    return phonebook



def write_txt(filename, phone_book):

    with open(filename,'w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s = ''
            for v in phone_book[i].values():

                s = s + v + ', '

            phout.write(f'{s[:-2]}')
            
def print_result(phone_book):
    # fields = ['ФАМИЛИЯ', 'ИМЯ', 'ТЕЛЕФОН', 'ОПИСАНИЕ']
    # print(*fields,'\n')
    # for val in phone_book:
    #     for i in fields:
    #         print(val.get(i), end = '')
    #     print('\n')
    print(tabulate(phone_book, headers = "keys", tablefmt = "pipe"))
    
    

def find_by_lastname(phone_book, last_name):
    new_phonebook = []
    for val in phone_book:
        if val.get('ФАМИЛИЯ') == last_name:
            new_phonebook.append(val)
    if new_phonebook == []:
        print("По данному запросу ничего не найдено")
    else:
        print(tabulate(new_phonebook, headers = "keys", tablefmt = "pipe"))
        
        

def find_by_lastname_and_number(phone_book, last_name, new_number):
    new = []
    for val in phone_book:
        if val.get('ТЕЛЕФОН') == new_number and val.get('ФАМИЛИЯ') == last_name:
            new.append(val)
    if new == []:
        print("По данному запросу ничего не найдено")
    else:
        print(tabulate(new, headers = "keys", tablefmt = "pipe"))
        
        
        
def delete_by_lastname(phone_book, lastname):
    new = []
    for i in range(len(phone_book)):
        if lastname in phone_book[i].values():
            del phone_book[i]
            break
    
    
def find_by_number(phone_book, number):
    new = []
    for val in phone_book:
        if val.get('ТЕЛЕФОН') == number:
            new.append(val)
    if new == []:
        print("По данному запросу ничего не найдено")
    else:
        print(tabulate(new, headers = "keys", tablefmt = "pipe"))
    
    
def add_user(phone_book):
    new_dict = {}
    fields=['ФАМИЛИЯ', 'ИМЯ', 'ТЕЛЕФОН', 'ОПИСАНИЕ']
    for i in fields:
        new_dict[i] = input(f'Введите {i}: ')
    phone_book.append(new_dict)
                    
work_with_phonebook()




    






















