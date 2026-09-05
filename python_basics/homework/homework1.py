# Найти сумму чисел трехзначного числа

number = int(input('Введите число: '))
a = number // 100
b = (number // 10) % 10
c = number % 10

result = a + b + c
print('Сумма чисел трехзначного числа - ', result)