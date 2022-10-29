weight = 8
height = 10
print('Марсозод находится на позиции: ', weight, ',', height)
command = input('Введите команду: ')
while command != '0':
    if command == 'W':
        height += 1
    elif command == 'S':
        height -= 1
    elif command == 'A':
        weight -= 1
    elif command == 'D':
        weight += 1
    if weight > 15:
        weight -= 1
    elif weight < 0:
        weight += 1
    if height > 20:
        height -= 1
    elif height < 0:
        height += 1
    print('Марсозод находится на позиции: ', weight, ',', height)
    command = input('Введите команду: ')