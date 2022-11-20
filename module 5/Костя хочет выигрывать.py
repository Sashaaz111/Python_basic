first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
third_num = int(input('Введите третье число: '))
if first_num == second_num == third_num:
    print(3)
elif first_num == second_num or second_num == third_num or first_num == third_num:
    print(2)
else:
    print(0)