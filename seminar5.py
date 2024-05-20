# Найти факториал числа n, используя рекурсию.

# def factor(n):
#     if n in [0, 1]:
#         return 1
#     return factor(n-1)*n

# n = int(input('Введите число: '))
# result = factor(n)
# print(f'Факториал числа {n}: ', result)


# Последовательность Фибоначчи через рекурсию.

def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)

n = int(input('Введите порядковый номер числа Фиббоначи: '))
result = fib(n)
print(f'Число Фибоначчи под номером {n}: ', result)
    