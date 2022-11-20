day = input('Введите день недели: ')
number_day = 1
for i in ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'):
    if i == day:
        print('Номер дня недели:', number_day)
        break
    else:
        number_day += 1