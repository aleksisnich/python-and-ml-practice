# n = 6
# list = [2, 10, 5, 4, 30, 45]
# a = []

# # начало цикла

# for i in range(n):
#     if list[i] % 5 == 0:
#         a.append(list[i])
        
# for i in list:
#     if i % 5 == 0:
#         a.append(i)

# max(a)

# print(max(a))

# n = int(input('Введите число элементов в списке: '))
# m = -3000

# for i in range(n):
#     cat = int(input('Введите число последовательности: '))
#     if cat % 5 == 0 and m < cat:
#         m = cat
        
# print(m)











# n = 7
# list = [8, 16, 6, 24, 55, 64, 33]
# sum = 0

# for i in range(n):
#     if list[i] % 6 == 0:
#         sum += list[i]
        
# print(sum)


# n = int(input())
# sum = 0 
# for i in range(n):
#     list = int(input())
#     if list % 6 == 0:
#         sum = sum + list
# print(sum) 




# n = 6
# list = [32, 6, 84, 26, 48, 33]
# count = 0
# for i in range(n):
#     if list[i] % 4 == 0:
#         count += 1
# print(count) 



















# Напишите программу, которая принимает на вход строку и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n. Для решения используем функцию split()

# word = input('Введите строку, каждый символ вводите через пробел: ')
# result = word.split()
# new = []
# print(result)

# for i in range(len(result)):
#     n = 1
#     for j in range(i + 1, len(result)):
#         if result[i] == result[j]:
#             result[j] = result[j] + '_' + str(n)
#             n += 1
# print(*result)

# Еще одно решение

# word = input('Введите строку, каждый символ вводите через пробел: ')
# new = ''

# for i in word.split():
#     if i not in new:
#         new += (f'{i} ')
#     elif i in new:
#         new += (f'{i}_{new.count(i)} ')
# print(new)

# Решение с помощью словаря

word = input('Введите строку, каждый символ вводите через пробел: ')
new = {}

for i in word.split():
    if i not in new:
        print(f'{i} ', end = ' ')
        #new[i] = 1
    elif i in new:
        print(f'{i}_{new[i]} ', end = ' ')
        #new[i] += 1
    new[i] = 1 + new.get(i, 0)      # вместо 123 и 126 строки

# Пользователь вводит текс(строка). 
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.

# text = input('Введите текст, разделителями между словами являются пробелы: ')
# new = text.split()
# count = 0 
# result = []

# for i in new:
#     if i not in result:
#             result.append(i)
#             count += 1
            
# print(count)

            
            











