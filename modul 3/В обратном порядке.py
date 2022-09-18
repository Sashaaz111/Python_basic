num = int(input('Введите число:'))
first_digit = num // 1000
second_digit = (num // 100) % 10
third_digit = (num % 100) // 10
fourth_digit = num % 10
print(str(fourth_digit) + str(third_digit) + str(second_digit) + str(first_digit))