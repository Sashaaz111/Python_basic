run = int(input('Введите пробег: '))
day = int(input('Введите сегодняшнее число: '))
summ_num_of_run = (run / 100) + (run / 10 % 10) + (run % 10)
if summ_num_of_run > day:
    print('Сброс.')
    run = 0
    print('Пробег:', run)
else:
    print('Сегодня не сломался.')
    print('Пробег:', run)
