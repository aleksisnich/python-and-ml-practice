# Задание 1. Сложение словарей

dict1 = {'One': 1, 'Two': 2, 'Three': 3}
dict2 = {'Four': 4, 'Five': 5, 'Six': 6}

def summ(a: dict, b: dict) -> dict:
    a = a.copy()
    for key, value in b.items():
        a[key] = value
    print(a)

summ(dict1, dict2)