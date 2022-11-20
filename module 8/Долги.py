debtors = int(input('Введите кол-во должников: '))
summ = 0
for i in range(0, debtors + 1, 5):
    print('Должник с номером', i)
    debt = int(input('Сколько должны? '))
    summ += debt
print('Общая сумма долга:', summ)