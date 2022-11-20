hour = int(input('Введите час: '))
if (hour > 7 and hour < 10) or (hour > 11 and hour < 14) or (hour > 14 and hour < 18) or (hour > 19 and hour < 22):
    print('Можно получить посылку')
else:
    print('Посылку получить нельзя')