num_Kostya = int(input('Кубик Кости: '))
num_owner = int(input('Кубик владельца: '))
if num_Kostya >= num_owner:
    difference = num_Kostya - num_owner
    print('Разность:', difference)
    print('Костя платит')
else:
    summ = num_Kostya + num_owner
    print('Сумма:', summ)
    print('Владелец платит')
print('Игра окончена')