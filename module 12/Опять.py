def minimum(num_1, num_2):
    minn = (num_1 + num_2 - abs(num_1 - num_2)) / 2
    print('Минимальное число:', minn)

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
minimum(num_1, num_2)