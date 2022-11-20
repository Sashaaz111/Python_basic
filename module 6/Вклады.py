x = int(input('Введите вклад: '))
p = int(input('Введите проценты: '))
y = int(input('Введите конечную сумму: '))
count = 0
while x < y:
    x = x + x * p // 100
    count += 1
print('Прошло лет:', count)