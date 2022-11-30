# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
# Учтите, что числа могут быть отрицательными
# Пример: 67.82 -> 23 (-0.56) -> 11

number = abs(float(input('Введите число:\n')))
digit_sum = 0
while number!=int(number):
    number = round(number*10, 10)
else: 
    number=int(number)
while number!=0:
    digit_sum += number % 10
    number = number // 10
print(digit_sum)