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

list = []
newlist =[]
n = int(input('Введите количество чисел в списке: '))
for i in range(n):
    newlist.append(i)
for i in range(n):
    list.append(int(input("Введите любое число: ")))
    
k = int(input('Введите число циклического сдвига: '))

for i in range(n):
    if i + k < n:
        newlist[i + k] = list[i]
    else:
        c = k - (n - i)
        newlist[c] = list[i] 
print(newlist)
        