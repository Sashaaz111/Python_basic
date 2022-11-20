lot_num = int(input('Введите кол-во чисел: '))
count = 0
for num in range(lot_num):
    number = int(input('Введите число: '))
    if number % 2 != 0:
        count += 1
print('Кол-во простых чисел:', count)

