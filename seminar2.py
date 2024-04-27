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

n = int(input('Введите число: '))
fib = 0
i = 1
count = 1

while fib < n:
    c = fib + i
    fib = i
    i = c 
    count = count + 1

if n == fib:
    print('Порядковый номер числа Фибоначчи:', count)
else:
    print('-1')

