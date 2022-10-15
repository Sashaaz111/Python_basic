count = 0
for i in range(30, 36):
    print('Людей в ', i, '-м секторе: ', )
    people = int(input())
    if people <= 10:
        print('Всё спокойно')
    elif people > 10:
        print('Нарушение! Слишеом много людей в секторе!')
        count += 1
print('Количество нарушений:', count)
