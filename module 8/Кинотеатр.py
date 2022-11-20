x = int(input('Введите число мальчиков: '))
y = int(input('введите число девочек: '))
ans = ''
if x > 2 * y or y > 2 * x or x == 0 or y == 0:
  print('Нет решений.')
elif y > x:
  n = y - x
  for i in range(n):
    ans += 'GBG'
  for i in range(x - n):
    ans += 'GB'
else:
  n = x - y
  for i in range(n):
    ans += 'BGB'
  for i in range(y - n):
    ans += 'BG'
print(ans)
