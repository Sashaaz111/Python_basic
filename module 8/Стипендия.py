educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы на проживание: '))
months = 10
summ_expenses = expenses
for i in range(1, months):
    expenses *= 1.03
    summ_expenses += expenses
family_pay = summ_expenses - months * educational_grant
print('У родителей необходимо попросить', family_pay)