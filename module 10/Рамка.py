width = int(input('Введите ширину: '))
height = int(input('Введите высоту: '))
for row in range(1, width + 1):
    for col in range(1, height + 1):
        if col == 1 or col == width:
            print('|', end = '')
        elif row == 1 or row == height:
            print('-', end = '')
        else:
            print(' ', end = '')
    print()

