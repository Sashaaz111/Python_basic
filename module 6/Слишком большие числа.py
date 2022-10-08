num = int(input('Введите число: '))
count = 0
while num > 0:
    num //= 10
    count += 1
print('Цифр в числе -', count)