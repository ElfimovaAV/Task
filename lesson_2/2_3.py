# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

N = int(input("Введите число: "))
number = 1

while number <= N:
    print(number, end=" ")
    number *= 2