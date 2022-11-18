def coin_area(x, y):
    if x >= -1 and x <= 1 and y >= -1 and y <= 1:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')

x = float(input('Введите координату x: '))
y = float(input('Введите координату y: '))
coin_area(x, y)