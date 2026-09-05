# Найти факториал числа n, используя рекурсию.

# def factor(n):
#     if n in [0, 1]:
#         return 1
#     return factor(n-1)*n

# n = int(input('Введите число: '))
# result = factor(n)
# print(f'Факториал числа {n}: ', result)


# Последовательность Фибоначчи через рекурсию.

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# n = int(input('Введите порядковый номер числа Фиббоначи: '))
# result = fib(n)
# print(f'Число Фибоначчи под номером {n}: ', result)
    

# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке. 
# В программме запрещается обьявлять массивы и использоватьо циклы (даже для ввода и вывода).


# def inver(n):
#     if n <= 0:
#         return ''
#     element = input('Введите число: ')
#     return inver(n-1) + element 

# print(inver(5))


# Домашнее задание

# Напишите программу, 
# которая на вход принимает два числа A и B, и возводит число A в целую степень B c помощью рекурсии.

# a = int(input('Введите число A: '))
# b = int(input('Введите число В: '))

# def degree(a, b):
#     if b == 0:
#         return 1
#     return a*degree(a, b-1)

# print(degree(a, b))

# Напишите рекурсивную функцию sum(a,b) возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются толькот +1 и -1.

# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))

# def sum(a, b):
#     if b > a:
#         c = a
#         a = b
#         b = c
#     if b == 0:
#         return a
#     return sum(a + 1, b-1)

# print(sum(a, b))

# ЛЕКЦИЯ 4

# В списке хранятся числа. Нужно выбрать только четные числа и составить список пар (число, квадрат числа).

# n = int(input('Введите количество чисел в списке: '))
# list = []
# new = []

# for i in range(n):
#     list.append(int(input('Введите число в списке: ')))
    
# def even_number(num, new):
#     for i in num:
#         if i % 2 == 0:
#             new.append((i, i*i))
#     return(new)

# print(even_number(list, new))
    
# Второй вариант

# n = int(input('Введите количество чисел в списке: '))
# list1 = []

# for i in range(n):
#     list1.append(int(input('Введите число в списке: ')))
    
# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# res = where(lambda x: x % 2 == 0, list1)
# res = select(lambda x: (x, x**2), res)
# print(res)
