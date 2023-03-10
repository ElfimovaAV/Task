# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

from random import randint

list_bashes = [randint(1, 11) for _ in range(int(input("Введите количество кустов черники: ")))]
print(list_bashes)

max_sum = 0

if (list_bashes[-1] + list_bashes[0] + list_bashes[1]) > max_sum:
    max_sum = list_bashes[-1] + list_bashes[0] + list_bashes[1]
if (list_bashes[-1] + list_bashes[-2] + list_bashes[0]) > max_sum:
    max_sum = list_bashes[-1] + list_bashes[-2] + list_bashes[0]

for i in range(1, len(list_bashes) - 1):
    if list_bashes[i-1] + list_bashes[i] + list_bashes[i+1] > max_sum:
        max_sum = list_bashes[i-1] + list_bashes[i] + list_bashes[i+1]
print(max_sum)

# ---2 способ-----
n = int(input())
arr = list()
for i in range(n):
    x = int(input())
    arr.append(x)

arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
arr_count.append(arr[-2] + arr[-1] + arr[0])
print(max(arr_count))