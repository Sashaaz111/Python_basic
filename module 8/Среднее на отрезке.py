a = int(input('Введите 1-е число: '))
b = int(input('Введите 2-е число: '))
c = int(input('Введите 3-е число: '))
average = 0
count = 0
for i in range(a, b + 1):
    if i % c == 0:
        average += i
        count += 1
print('Среднее арифметическое:', average / count)
