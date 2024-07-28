# Задание 1. Сложение словарей

dict1 = {'One': 1, 'Two': 2, 'Three': 3}
dict2 = {'Four': 4, 'Five': 5, 'Six': 6}

def summ(a: dict, b: dict) -> dict:
    a = a.copy()
    for key, value in b.items():
        a[key] = value
    print(a)

summ(dict1, dict2)

keys = ['One', 'Two', 'Three']
values = [1, 2, 3]
def make_dic(list1: list, list2: list) -> dict:
    res = {}
    for i in range(len(list1)):
        res[i] = list2[i]
    #print(res)
make_dic(keys, values)