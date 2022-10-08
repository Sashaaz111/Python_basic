num = int(input('Введите кол-во дней: '))
count = 0
while num != 0:
    if num % 2 == 0:
        count += 1
    num = int(input('Введите кол-во дней: '))
print('Кол-во месяцев:', count)