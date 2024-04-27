# Первое задание. Вычислить значение n! при n > 0. Использовать цикл while.

n = int(input('Введите целое число: '))
i = 2
n_factorial = 1
if n > 0:
    while i <= n:
        n_factorial = n_factorial * i
        i = i + 1
    print('n! = ', n_factorial)
elif n == 0:
        n_factorial = 1
        print('n! = ', n_factorial)
else:
    print("Число не может быть отрицательным")
