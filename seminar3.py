# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# list = []
# n = int(input('Введите количество чисел в списке: '))
# for i in range(n):
#     list.append(int(input("Введите любое число: ")))
# for i in range(len(list)-1):
#     j = i + 1
#     while j < len(list):
#             if list[i] == list[j]:
#                 list.pop(j)
#                 j -= 1
#                 # print(list)
#                 # print(len(list))
#             j += 1
# print('Количество различных чисел в списке:', len(list))

# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг-циклический) на K элементов вправо, k > 0.

# list = []
# newlist =[]
# n = int(input('Введите количество чисел в списке: '))
# for i in range(n):
#     newlist.append(i)
# for i in range(n):
#     list.append(int(input("Введите любое число: ")))
    
# k = int(input('Введите число циклического сдвига: '))

# for i in range(n):
#     if i + k < n:
#         newlist[i + k] = list[i]
#     else:
#         c = k - (n - i)
#         newlist[c] = list[i] 
# print(newlist)


# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. 
# Теперь он использует их в качестве серверов "Пегого дудочника". 
# Помогите владельцу фирмы отыскать все зараженные холодильники.

# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, 
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, 
# главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, 
# нумерация начинается с единицы

# Формат входных данных
# В первой строке подаётся число n – количество холодильников. В последующих строках вводятся строки, 
# содержащие латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.

# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. 
# Если таких холодильников нет, ничего выводить не нужно.


# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1: 
# 1 2 3

# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8
        
        
# bag = 'anton'
# result = []
# n = int(input('Введите количество холодильников: '))
# for i in range(n):
#     frozen = input("Введите шифр для каждого холодильника: ")
#     res = ''
#     for j in bag:
#         #print(j)
#         if j in frozen:
#             res = res + j
#     # print(res)
#     if res == 'anton':
#         result.append(i + 1)
# print(*result)

# ВТОРОЙ СПОСОБ        
# frozen = []
# bag = 'anton'
# result = []
# string = ''
# n = int(input('Введите количество холодильников: '))
# for i in range(n):
#     frozen.append(input("Введите шифр для каждого холодильника: "))
# #print(len(frozen))
# for i in range(n):
#     string = frozen[i]
#     res = ''
#     for j in bag:
#         if j in string:
#             res = res + j
#     if res == bag:
#         result.append(i + 1)
# print(*result)

# Еще способ
# n = int(input())
# list1 = []
# for i in range(n):
#     a = input()
#     if 'a' in a:
#         a = a[a.find('a'):]
#         if 'n' in a:
#             a = a[a.find('n'):]
#             if 't' in a:
#                 a = a[a.find('t'):]
#                 if 'o' in a:
#                     a = a[a.find('o'):]
#                     if 'n' in a:
#                         list1.append(i + 1)                   
# print(*list1)


# И еще способ
# n=int(input())
# f=[]
# hacker =  ['a', 'n', 't', 'o', 'n','']
# count=0
# otvet=[]
# for i in range(n):
#     u=input()
#     f.append(u)
# for i in range(len(f)): 
#     hacker =  ['a', 'n', 't', 'o', 'n','']          
#     for j in range(len(f[i])):         
#         if f[i][j]==hacker[0]:
#             hacker.pop(0)            
#         if hacker==['']: 
#             count=1+i        
        
#             otvet.append(count)
          
            
            
#             break

# print(*otvet)

# ДОМАШНЯЯ РАБОТА

# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1...N].
# Пользователь в первой строке вводит натуральное число N - количество элементов в массиве. 
# В последующих строках записаны N целых чисел A. Последняя строка содержит число X.

# N = int(input('Введите количество чисел в массиве: '))
# A = []
# count = 0
# for i in range(N):
#     A.append(int(input("Введите любое число в массив A: ")))
# X = int(input('Какое число ищем? '))

# for i in A:
#     if i == X:
#         count += 1

# print('Количество чисел X в массиве A: ', count)


# Требуется найти в массиве A[1...N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит вводит натуральное число N - количество элементов в массиве. 
# В последующих строках записаны N целых чисел A. Последняя строка содержит число X.

# N = int(input('Введите количество чисел в массиве: '))
# A = [] 
# for i in range(N):
#     A.append(int(input("Введите любое число в массив A: ")))
# X = int(input('Какое близкое число ищем? ')) 
# approx = A[0]
# for i in range(N - 1):
#     if abs(approx - X) >= abs(A[i + 1] - X):
#         approx = A[i + 1]

# print('Ближайшее значение: ', approx)



# Задача про Скрабл.

# word = str(input('Введите слово на русском или английском: '))
# count = 0
# dict = {1 : 'AEIOULNSTRАВЕИНОРСТaeioulnstrавеинорст', 2 : 'DGДКЛМПУdgдклмпу', 3 : 'BCMPБГЁЬЯbcmpбгёья', 4 : 'FHVWYЙЫfhvwyйы', 5 : 'KЖЗХЦЧkжзхцч', 8 : 'JXШЭЮjxшэю', 10 : 'QZФЩЪqzфщъ'}

# for i in range(len(word)):
#     for j in dict:
#         element = dict[j]
#         if word[i] in element:
#             count = count + j
            
# for i in word:
#     for j in dict:
#         if i in dict[j]:
#             count = count + j

# print(count)