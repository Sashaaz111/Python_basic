n = int(input('Введите число членов ряда: '))
sum = 1
for i in range(1, n + 1):
  sum += (-1) ** i * (1 / 2 ** i)
print('Сумма ряда равна', sum)
