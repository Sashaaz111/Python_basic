n = int(input('Введите число: '))
ans = 1
for i in range(1, n + 1):
    ans *= i
print('Факториал числа', n, 'равен', ans)