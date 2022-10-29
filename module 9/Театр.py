row = int(input('Введите кол-во рядов: '))
seat = int(input('Введите кол-во сидений: '))
meters = int(input('Введите кол-во метров между рядами: '))
print('Сцена')
for i in range(1,row + 1):
    print(('=' * seat) + ' ' + ('*' * meters) + ' ' + ('=' * seat))