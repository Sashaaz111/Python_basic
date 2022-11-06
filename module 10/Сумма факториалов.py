num = int(input('Введите число: '))
mult = 1
fact = 0
for row in range(1, num + 1):
    mult *= row
    fact += mult
print(fact)