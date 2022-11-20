def reverse(num):
    rev_num = ''
    while num != 0:
        rev_num += str(num % 10)
        num //= 10
    print('Число наоборот:', rev_num)

while 1 < 2:
    num = int(input('Введите число: '))
    if num == 0:
        print('Программа завершена')
        break
    reverse(num)