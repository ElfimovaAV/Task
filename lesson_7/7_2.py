# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

rows = int(input())
columns = int(input())
def print_operation_table(operation, num_rows, num_columns):
    for i in range(1, num_rows + 1):
        table = []
        for j in range(1, num_columns + 1):
            table.append(str(operation(i, j)))
        print(''.join(f'{e:<5}' for e in table)) # print(f"{operation(i, j):4}", end=" ")

print_operation_table(lambda x, y: x * y, rows, columns)