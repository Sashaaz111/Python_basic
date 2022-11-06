N = int(input('Введите кол-во чисел: '))
max = 0
sum = 0
for num in range(N):
    number = int(input('Введите число: '))
    while number > 0:
        sum += number % 10
        number //= 10
    if sum > max:
        max = sum
    sum = 0
print(max)