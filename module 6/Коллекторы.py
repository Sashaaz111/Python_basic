name = input('Введите имя: ')
debt = int(input('Введите сумму долга: '))
print(name, ', ваша задолженность составляет', debt, 'рублей')
while debt > 0:
    print('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?')
    sum = int(input())
    if (sum >= debt):
        debt -= sum
    if (debt > 0):
        print('Маловато,', name, '. Давайте ещё раз.')
    else:
        print('Отлично,', name, '! Вы погасили долг. Спасибо!')

