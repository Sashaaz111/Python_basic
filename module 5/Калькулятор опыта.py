exp = int(input('Введите кол-во опыта: '))
level = 1
if exp >= 0 and exp < 1000:
    print('Ваш уровень:', level)
elif exp >= 1000 and exp < 2500:
    level += 1
    print('Ваш уровень:', level)
elif exp >= 2500 and exp < 5000:
    level += 2
    print('Ваш уровень:', level)
elif exp >= 5000:
    level += 3
    print('Ваш уровень:', level)

