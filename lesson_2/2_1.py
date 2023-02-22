# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

coins = int(input("Введите число монеток: "))
count = 0
rest = coins - count
for i in range(coins):
    side = int(input("Введите 0 или 1 (решка или орёл): "))
    if side == 0:
        count +=1
if count < rest:
    print(f"Нужно перевернуть {count} монет")
else:
    print(f"Нужно перевернуть {rest} монет")