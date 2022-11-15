def sumNums(num):
    summ = 0
    while num != 0:
        summ += num % 10
        num //= 10
    print('Сумма цифр:', summ)

def maxNum(num):
    maxx = 0
    while num != 0:
        if num % 10 > maxx:
            maxx = num % 10
        num //= 10
    print('Максимальная цифра:', maxx)
2
def minNum(num):
    minn = 10e9
    while num != 0:
        if num % 10 < minn:
            minn = num % 10
        num //= 10
    print('Минимальная цифра:', minn)

while 1 < 2:
    num = int(input('Введите число: '))
    action = int(input('1 - вывести сумму цифр, 2 - максимальная цифра, 3 - минимальная цифра: '))
    if action == 1:
        sumNums(num)
    elif action == 2:
        maxNum(num)
    elif action == 3:
        minNum(num)
    else:
        print('Некорректный ввод')