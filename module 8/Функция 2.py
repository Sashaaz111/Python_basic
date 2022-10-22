begin = int(input('Введите начало отрезка: '))
end = int(input('Введите конец отрезка: '))
for x in range(end, begin - 1, -1):
    y = x ** 3 + 2 * x ** 2 - 4 * x + 1
    print('В точке', x, 'функция равна:', y)