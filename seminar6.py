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

n = int(input('Введите число: '))
a = n - 1

def simple(number1, number2):
    if number1 == 1:
        return 'Уникальное число'
    if number2 == 1:
        return True
    if number1 % number2 != 0:
        return  simple(number1, number2 - 1)
    return False 
        

print(simple(n, a))   

    
    