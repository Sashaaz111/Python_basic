mark = int(input('Введите число: '))
plus = 0
minus = 0
while mark >= -100 and mark <= 100:
    if mark > 0 and mark <= 100:
        plus += 1
    elif mark < 0 and mark >= -100:
        minus += 1
    elif mark == 0:
        break
    mark = int(input('Введите число: '))

print('Кол-во положительных чисел:', plus)
print('Кол-во отрицательных чисел:', minus)
