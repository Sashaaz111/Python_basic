length = int(input('Введите длину: '))
exclamation_point = int(input('Введите кол-во восклицательных знаков: '))
for i in range(1):
    print(('~' * ((length - exclamation_point) // 2)) + ('!' * exclamation_point) + ('~' * ((length - exclamation_point) // 2)))

