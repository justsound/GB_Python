# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
#  чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

""" def get_coins(n):
    return [int(input("Введите число 0 или 1:")) for i in range(n)]

def find_count_of_turns (list):
    return min (list.count(True), list.count(False))
l = get_coins(int(input("Введите количество монет:")))

print(find_count_of_turns(l)) """

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
#  а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
""" S = int(input("Введите сумму чисел:"))
P = int(input("Введите произведение чисел:"))
for i in range(S):
    for j in range(S):
        if i + j == S and i*j == P:
            print(f"Ваши числа: {i}, {j}.") """

# X + Y = S
# X*Y = P

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

""" N = int(input("Введите число N:"))
i = 0
while 2**i <=N:
    print(2**i, end = " ")
    i +=1 """





