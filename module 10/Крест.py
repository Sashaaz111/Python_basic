value = int(input('Введите значение ширины и высоты: '))
for row in range(value):
    for col in range(value):
        if col == row:
            print('^', end = '')
        elif col == -row + value - 1:
            print('^', end = '')
        else:
            print(' ', end = ' ')
    print()