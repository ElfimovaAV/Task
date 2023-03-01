# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в списке A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai.
# Последняя строка содержит число X

list_nums = [int(i) for i in input("Введите элементы списка: ").split()]
x = int(input("Введите искомое значение: "))
print(sum([list_nums[i] == x for i in range(len(list_nums))]))



# 2 способ -------
list_1 = [int(input("Введите элементы списка: ")) for _ in range(int(input("Введите количество элементов списка: ")))]
print(list_1.count(int(input("Введите искомое значение: "))))

# 3 способ -------
from random import choices

num = int(input("Введите количество элементов списка: "))
list_2 = choices(range(num * 2), k=num)
print(list_2)

result = list_1.count(int(input("Введите искомое значение: ")))
print(result)