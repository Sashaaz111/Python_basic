x = int(input('Введите число: '))
upper = 1
lower = 1
for i in range(1, 7):
  relation = 2 ** i
  upper *= x - relation + 1
  if x - relation == 0:
    print('Делить на 0 нельзя')
    break
  else:
    lower *= x - relation
else:
  print('Выражение равно:', upper / lower)
