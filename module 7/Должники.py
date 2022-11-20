count = 0
for numbers in range(10):
    num = int(input('Введите число: '))
    if num >= 0 and num % 2 == 0:
        count += 1
print('Одновременно чётных и положительных: ', count)