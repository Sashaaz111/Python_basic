def NOD(num_1, num_2):
    while num_1 != num_2:
        if num_1 > num_2:
            num_1 -= num_2
        elif num_2 > num_1:
            num_2 -= num_1
    print('НОД =', num_1)

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
NOD(num_1, num_2)