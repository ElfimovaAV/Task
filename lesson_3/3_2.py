# Задача 18: Требуется найти в массиве A[1..N] самый близкий меньший по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в списке. В
# последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X

list_nums = [int(i) for i in input("Введите элементы списка: ").split()]
x = int(input("Введите искомое значение: "))

min_diff_bigger = min_diff_smaller = max(list_nums)
min_ind_bigger = min_ind_smaller = 0

for i in range(len(list_nums)):
    if 0 <= (list_nums[i] - x) < min_diff_bigger:
        min_diff_bigger = list_nums[i] - x
        min_ind_bigger = i
    if 0 > (list_nums[i] - x) > -min_diff_smaller:
        min_diff_smaller = x - list_nums[i]
        min_ind_smaller = i

if min_diff_smaller <= min_diff_bigger:
    print(list_nums[min_ind_smaller])
else:
    print(list_nums[min_ind_bigger])