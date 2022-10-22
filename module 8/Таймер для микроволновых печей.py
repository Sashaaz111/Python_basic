second = int(input('Введите количество секунд: '))
for i in range(second, -1, -1):
  reverse_timer = int(input('Хотите прервать разогрев? (1 - да, 0 - нет)? '))
  if reverse_timer == 1:
    print('Ваша еда готова, можете забрать. До конца осталось', i, 'секунд.')
    break
  else:
    print('До конца разогрева осталось', i, 'секунд.')
else:
  print('Ваша еда готова, осторожно, горячo!')
