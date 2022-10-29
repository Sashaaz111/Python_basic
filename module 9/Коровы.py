text = input('Введите символы: ')
sum = 0
num = 1
for i in text:
    if i == 'b':
        sum += num * 2
        num += 1
    elif i == 'a':
        num += 1
print('Литров молока за день:', sum)