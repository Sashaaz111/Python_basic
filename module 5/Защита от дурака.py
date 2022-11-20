num = int(input('Введите число: '))
if (num >= 10 and num < 100) or (num > -100 and num <= -10):
    print('Число двузначное')
else:
    print('Число не двузначое')