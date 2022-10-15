a = int(input('Введите число: '))
b = int(input('Введите число: '))
medium_of_num = 0
count = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        medium_of_num += i
        count += 1
medium_of_num /= count
print('Среднее арифметическое чисел, кратных 3, равно', medium_of_num)

