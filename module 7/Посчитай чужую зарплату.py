medium_salary = 0
for months in range(12):
    month_salary = int(input('Введите месячную зарплату: '))
    medium_salary += month_salary
print('Средняя годовая зарплата:', medium_salary / 12)