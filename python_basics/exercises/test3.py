# Задача с партами. У нас 3 класса: в 1 - 20, во 2 - 21, в 3 - 22 человека. Сколько парт минимум?

class1 = int(input('Введите количество человек в первом классе: '))
class2 = int(input('Введите количество человек во втором классе: '))
class3 = int(input('Введите количество человек в третьем классе: '))

number_one = 2

resuls_for_1 = abs(-class1 // 2)
resuls_for_2 = abs(-class2 // 2)
resuls_for_3 = abs(-class3 // 2)

quantity = resuls_for_1 + resuls_for_2 + resuls_for_3

print('Минимальное количество парт', quantity)