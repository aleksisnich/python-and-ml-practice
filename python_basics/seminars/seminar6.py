# №1 Определить при помощи рекурсии полиндром или нет слово. 
# А-ля шалаш, казак. В обратную сторону можно развернуть. 

# word = input('Введите слово или набор цифр: ')
# n = len(word)
# i = 0

# def poly(n, i,  string):
#     if n == 0:
#         return ''
#     return poly(n - 1, i + 1, string) + string[i]

# print(poly(n, i, word))
# if word == poly(n, i, word):
#     print('Слово полиндром!')
# else:
#     print('Слово не полиндром')
    
# Дополнительное решение
# word = input('Введите слово или набор цифр: ')

# def poly(string):
#     if len(string) <= 1:
#         return True
#     if string[0] == string[-1]:
#         return poly(string[1:-1])
#     return False

# print(poly(word))
                
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым. 
# Делитель 1 и само на себя. 1 - не является простым числом.

# n = int(input('Введите число: '))
# a = n - 1

# def simple(number1, number2):
#     if number1 == 1:
#         return 'Уникальное число'
#     if number2 == 1:
#         return True
#     if number1 % number2 != 0:
#         return  simple(number1, number2 - 1)
#     return False 
        

# print(simple(n, a))   


# Два различных числа m и n называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Вывести все пары дружественных чсиел для числа k, не превосходящие его.

k = int(input('Введите число k: '))

dict_1 = {}

for i in range(1, k):
    for j in range(1, i//2 + 1):
        if i % j == 0:
            dict_1[i] = dict_1.get(i, 0) + j

for i, sumdiv in dict_1.items():
    if i < sumdiv and i == dict_1.get(sumdiv, False) and sumdiv == dict_1[i]:
        print(i, sumdiv)

# Домашнее задание. 
# Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума). 
# На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# n = int(input('Введите количество чисел в списке: '))
# listik = []
# min_number = 0
# max_number = 10
# for i in range(n):
#     listik.append(int(input('Введите элемент списка: ')))

# for i in range(n):
#     if min_number <= listik[i] <= max_number:
#         print(i)

# Заполните массив элементами арифметической прогрессии. Её первый элемент a1, 
# разность d и количество элементов n будет задано автоматически. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# a1 = int(input('Введите первое число прогрессии: '))
# d = int(input('Введите разность: '))
# n = int(input('Введите количество чисел: '))

# # listik = []

# for i in range(1, n + 1):
#     print(a1 + (i - 1)*d)
#     # listik.append(a1 + (i - 1)*d)
    
# print(listik)

    
    