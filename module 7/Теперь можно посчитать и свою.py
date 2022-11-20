tmp = 0
for i in range(10):
  salary = int(input('Введите зарплату за этот месяц: '))
  if tmp < salary:
    tmp = salary
  else:
    print('Зарплата неупорядочена по возростанию.')
    break
else:
  print('Зарплата упорядочена по возростанию.')
