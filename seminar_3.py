# Дан список чисел. Определите, сколько в нем встречается различных чисел.
""" n = int(input("Введите число элементов:"))
list_1 = [int(input()) for item in range(n)]
list = set(list_1)
print(len(list))
 """
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

""" n = int(input("Введите число элементов:"))
list_1 = [int(input()) for item in range(n)]
k = int(input("Введите число на которое требуется сдвинуть последовательность"))
for i in range(k):
    list_1.append(list_1.pop(0))
print(list_1) """

# Напишите программу для печати всех уникальных значений в словаре

""" dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},  {" VIII ":" S007 "}]
list = []
for i in range(len(dictionary)):
    list += dictionary[i].values()
print(set(list)) """

# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего 

""" n = int(input("Введите число элементов:"))
list_1 = [int(input()) for item in range(n)]
count = 0
for i in range(len(list_1)-1):
    if list_1[i] < list_1[i+1]:
            count +=1
print(count) """

# 1.Создайте список из случайных чисел. Найдите номер его последнего локального максимума 
# (локальный максимум — это элемент, который больше любого из своих соседей).
""" import random

n = int(input("Введите число элементов:"))
list_1 = [random.randint(-50,50) for item in range(n)]
print(list_1)
local_max = list_1[0]
for i in range(1, len(list_1)-1):
    if list_1[i-1] < list_1[i] > list_1[i + 1]:
        local_max = i
print(local_max) """

# 3.Создайте список из случайных чисел. Найдите второй максимум.

""" import random

n = int(input("Введите число элементов:"))
list = [random.randint(-50, 50) for item in range(n)]
print(list)
list.sort()
print(list[-2]) """
    

""" Напишите программу, которая заполняет массив из N элементов членами арифметической прогрессии с начальным значением X и разностью D в обратном порядке,
так чтобы последний элемент был равен X .

Входные данные
Входная строка содержит три целых числа: начальное значение X , разность D и размер массива N , разделённые пробелом.
Гарантируется, что 0 < N ≤ 10000 .

Выходные данные
Программа должна вывести содержимое массива: N первых членов арифметической прогрессии с начальным значением X и разностью D в обратном порядке,
так что последний элемент массива равен X . """

n = int(input("Введите количество элементов:"))
x = int(input("Введите начальное значение:"))
d = int(input("Введите разность:"))
spisok = [x]
for i in range(n-1):
    spisok.insert(0, x+d)
    x = x+d
# print(list[::-1])    
# spisok.sort(reverse=True)
print(spisok)

