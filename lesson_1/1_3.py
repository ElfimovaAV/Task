# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
# и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

number = str(input('Введите шестизначный номер билета: '))
if (int(number[0])+int(number[1])+int(number[2])) == (int(number[3])+int(number[4])+int(number[5])):
    print('Этот билет счастливый!')
else:
    print('Этот билет не счастливый!')

# sum_first = int(number[0])+int(number[1])+int(number[2])
# sum_second = int(number[3])+int(number[4])+int(number[5])
# print(f'The ticket is lucky: {sum_first == sum_second}')   то есть в выводе будет The ticket is lucky: true
# или The ticket is lucky: false

# -----------second solution
number = int(input('Введите шестизначный номер билета: '))

sum_first = 0
sum_last = 0

while number:
    digit = number % 10
    if number > 999:
        sum_first += digit
    else:
        sum_last += digit
    number //= 10

print(f'The ticket is lucky: {sum_first == sum_last}')