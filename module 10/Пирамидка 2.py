height = int(input('Введите количество уровней: '))
odd = 1
tab = ' ' * (height - 1)
for row in range(1, height + 1):
    print(tab * (height - row), end = '')
    for col in range(row):
        print(('{:' + str(len(tab)) + '}').format(odd), end = tab)
        odd += 2
    print()