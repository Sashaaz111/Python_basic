num = int(input('Введите число: '))
num1 = num // 1000
num2 = num % 1000
while num >= 100000 and num < 1000000:
    sum1 = num1 % 10 + num1 // 10 % 10 + num1 // 100
    sum2 = num2 % 10 + num2 // 10 % 10 + num2 // 100
    if sum1 == sum2:
        print('Счастливый')
        break
    else:
        print('Не счастливый')
        break