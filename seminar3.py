# Дан список чисел. Определите, сколько в нем встречается различных чисел.

list = []
n = int(input('Введите количество чисел в списке: '))
for i in range(n):
    list.append(int(input("Введите любое число: ")))
for i in range(len(list)-1):
    j = i + 1
    while j < len(list):
            if list[i] == list[j]:
                list.pop(j)
                j -= 1
                # print(list)
                # print(len(list))
            j += 1
print('Количество различных чисел в списке:', len(list))
