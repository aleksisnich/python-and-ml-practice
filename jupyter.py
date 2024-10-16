# Задание 1. Сложение словарей

# dict1 = {'One': 1, 'Two': 2, 'Three': 3}
# dict2 = {'Four': 4, 'Five': 5, 'Six': 6}
#
# def summ(a: dict, b: dict) -> dict:
#     a = a.copy()
#     for key, value in b.items():
#         a[key] = value
#     print(a)
#
# summ(dict1, dict2)

# keys = ['One', 'Two', 'Three']
# values = [1, 2, 3]
# def make_dic(list1: list, list2: list) -> dict:
#     res = {}
#     for i in range(len(list1)):
#         res[i] = list2[i]
#     #print(res)
# make_dic(keys, values)


# Домашняя работа - семинар 1

# Дан список adv с затратами на рекламу.
# Но в данных есть ошибки, некоторые затраты имеют отрицательную величину.
# Удалите такие значения из списка и посчитайте суммарные затраты.
# Запишите их в переменную x.
# Используйте list comprehensions.

# adv = [100, 125, -90, 345, 655, -1, 0, 200]
#
# new = [adv[i] for i in range(len(adv)) if adv[i] >= 0]
# x = sum(new)
#
# print(x)

# Задание 2
# На складе лежат разные фрукты в разном количестве.
# Нужно написать функцию total_fruits, которая на вход принимает любое количество названий фруктов и их количество,
# а возвращает общее количество фруктов на складе.
#
# можно решить через *kwargs

# def total_fruits(**fruits):
#     x = sum(fruits.values())
#     return x
#
# print(total_fruits(apples=10, bananas=5, oranges=8))

# Задание 3

# Даны два списка: дата покупки dates, суммы покупок по датам income.
# Найти итоговую сумму всех покупок в ноябре и сохранить ее в переменную x.
# Используйте list comprehensions.

# dates = ['2021-10-01', '2021-11-05', '2021-12-10', '2021-11-12']
# income = [100, 200, 300, 100]
#
# new = [income[i] for i in range(len(dates)) if '11' in dates[i].split('-')]
# x = sum(new)
#
# print(x)

# Задание 4

# Найдите выручку компании в зависимости от месяца. Для этого напишите функцию calc_income_by_month(),
# которая на вход принимает список с датами и список с выручкой, а на выходе словарь, где ключи - это месяцы,
# а значения - это выручка. Используйте аннотирование типов.

# def calc_income_by_month(dates: list, incomes: list) -> dict:
#     res = {}
#     for i in range(len(dates)):
#         new = dates[i].split('-')
#         for j in range(len(new)):
#             if j == 1 and new[j] not in res:
#                 res[new[j]] = incomes[i]
#             elif j == 1 and new[j] in res:

#                 res[new[j]] = res[new[j]] + incomes[i]
#     return res
#
# dates = ['2021-10-01', '2021-11-05', '2021-12-10', '2021-12-10']
# incomes = [100, 200, 300, 150]
#
# print(calc_income_by_month(dates, incomes))



