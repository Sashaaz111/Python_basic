price = int(input('Введите стоимость: '))
area = int(input('Введите площадь: '))
if (area >= 100 and price <= 10) or (area >= 80 and price <= 7):
    print('Квартира подходит')
else:
    print('Квартира не подходит')