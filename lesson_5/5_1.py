# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def degree(n, m):
    if m == 0:
        return 1
    return degree(n, m - 1) * n

num_1 = int(input())
num_2 = int(input())
print(degree(num_1, num_2))

# 2 способ
def pow_num(a, b):
    if b == 0:
        return 1
    if b < 0:
        return pow_num(a, b + 1) * 1 / a
    return pow_num(a, b - 1) * a

print(pow_num(int(input()), int(input())))
