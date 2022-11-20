income = int(input('Введите доход: '))
if income < 10000:
    tax = (10000 * 13) / 100
    print('Налог:', tax)
elif income >= 10000 and income <= 50000:
    tax = (((income - 10000) * 20) / 100) + ((10000 * 13) / 100)
    print('Налог:', tax)
else:
    tax = (((income - 50000) * 30) / 100) + (((income - 50000 - 10000) * 20) / 100) + ((10000 * 13) / 100)
    print('Налог:', tax)