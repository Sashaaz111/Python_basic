N = int(input('Введите число: '))
for i in range(N, 0, -1):
    for j in range(N, 0, -1):
        if i - 1 < j:
            print(j, end = '')
        else:
            print('.', end = '')
    for j in range(1, N + 1):
        if i - 1 < j:
            print(j, end = '')
        else:
            print('.', end = '')
    print()
