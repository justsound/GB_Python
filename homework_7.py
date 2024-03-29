# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам Парам пам-пам

# song = input().strip().lower().split( )
# t = []
# for word in song:
#     t.append(len([x for x in word if x in "уеыаоэяиюё"]))
# if len(set(t)) == 1:
#     print("Парам пам-пам")
# else:
#     print("Пам парам")

# вариант2
# f = lambda x: sum(1 for i in x if i in 'уеыаоэяиюё')
# t = f(song[0])
# if all([f(i) == t for i in song]):
#     print("Парам пам-пам")
# else:
#     print("Пам парам")


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, row, column):
    for i in range(1, row + 1):
        print(end = '\n')
        for j in range(1, column+1):
            if i != 1 and j != 1:
                print(f'\t{operation(i,j)}', end = '')
            elif i == 1:
                print(f'\t{j}', end = '')
            else:
                print(i, end = '\t')
    
row, column = (int(i) for i in input().split())
print_operation_table(lambda row, column: row / column, row, column)

""" def show_table(table: list[list[int]]) -> None:
    '''Просто красиво печает матрицу)'''
    print('\n'.join('\t'.join(map(str, row)) for row in table))


def print_operation_table(oper: callable,
                          num_columns: int = 4,
                          num_rows: int = 4) -> None:
    '''Выводит таблицу для чисел с заданной оперцией oper,
    числом столбцов num_columns и строк num_rows'''
    table = [list(range(i, i+num_columns)) for i in range(1, num_rows+1)]
    # show_table(table)
    for i in range(1, len(table)):
        for j in range(1, len(table[i])):
            table[i][j] = oper(table[i][0], table[0][j])
    show_table(table) """
