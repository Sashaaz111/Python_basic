width = int(input('Введите ширину: '))
height = int(input('Введите высоту: '))
for row in range(1, width + 1):
    for col in range(1, height + 1):
        if col == 1 or col == height:
            print('|', end = '')
        elif row == 1 or row == width:
            print('-', end = '')
        else:
            print(' ', end = '')
    print()

