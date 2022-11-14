def summa_n(N):
    summN = 0
    for i in range(1, N + 1):
        summN += i
    print('Я знаю, что сумма чисел от 1 до', N, 'равна', summN)

N = int(input('Введите число: '))
summa_n(N)