# # Первое задание. Вычислить значение n! при n > 0. Использовать цикл while.

# n = int(input('Введите целое число: '))
# i = 2
# n_factorial = 1
# if n > 0:
#     while i <= n:
#         n_factorial = n_factorial * i
#         i = i + 1
#     print('n! = ', n_factorial)
# elif n == 0:
#         n_factorial = 1
#         print('n! = ', n_factorial)
# else:
#     print("Число не может быть отрицательным")

# Второе задание. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что фи(n) = A. Если A не является числом Фибоначчи, выведите число -1.

# n = int(input('Введите число: '))
# fib = 0
# i = 1
# count = 1

# while fib < n:
#     c = fib + i
#     fib = i
#     i = c 
#     count = count + 1

# if n == fib:
#     print('Порядковый номер числа Фибоначчи:', count)
# else:
#     print('-1')

# Дана строка а-ля "ОРРООРРРО", нужно вывести максимальное количество Р, идущих подряд. 
# Если выпавших Р нет, то необходимо вывести число 0.

# op = str(input('Введите строку, содержащую О и Р: '))
# n = len(op)
# i = 0
# count = 0
# maxcount = 0 
# maxnumber = 0
# while i < n:
#     if op[i] == 'Р':
#         count = count + 1
#         maxcount = count
#         if  maxcount > maxnumber:
#             maxnumber = maxcount
#     else: 
#         count = 0
#         maxcount = count
#     i += 1
# if maxnumber == 0:
#     print(0)
# print('Максимальное количество Р, идущих подряд: ', maxnumber)

# Пользователь вводит число N - кол-во дней (диапазон от 1 до 100). 
# В следующих строках располагается N целых чисел. Каждое число - температура (от -50 до 50). 
# Вычислить количество дней с положительной температурой подряд. 

# N = int(input('Введите количество дней: '))
# i = 1
# count = 0
# maxcount = 0
# maxnumber = 0
# if N >= 1 and N <= 100:
#     while i <= N:
#         temp = int(input('Введите температуру за каждый день: '))
#         if temp >= -50 and temp <= 50:
#             if temp >= 0:
#                 count = count + 1
#                 maxcount = count
#                 if  maxcount > maxnumber:
#                     maxnumber = maxcount
#             else:
#                 count = 0
#                 maxcount = count
#         else:
#             print('Температура должна быть в диапазоне от -50 до 50 градусов') 
#         i += 1
# else:
#     print('Количество дней должно быть в диапазоне от 1 до 50')
    
# print('Количество дней с положительной температурой подряд: ', maxnumber) 

# Пользователь вводит количество арбузов N разного веса. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число - это масса соответствующего арбуза. Надо выбрать самый легкий и самый тяжелый.

N = int(input('Введите количество арбузов: '))
i = 2
mass = int(input('Введите массу первого арбуза: '))
maxnumber = mass
minnumber = mass
while i <= N:
    mass = int(input('Введите массу каждого арбуза, начиная со второго: '))
    if mass > maxnumber:
        maxnumber = mass
    elif mass < minnumber:
        minnumber = mass
    i += 1    
print('Максимальная масса арбуза: ', maxnumber) 
print('Минимальная масса арбуза: ', minnumber) 
        
        
