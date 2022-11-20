first_price = int(input('Введите цену 1-го стула: '))
second_price = int(input('Введите цену 2-го стула: '))
third_price = int(input('Введите цену 3-го стула: '))
summ = first_price + second_price + third_price
if summ > 10000:
    summ -= summ * 10 / 100
    print('Сумма равна', summ)
else:
    print('Сумма равна', summ)