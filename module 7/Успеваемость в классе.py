n = int(input('Введите кол-во человек: '))
count_of_3 = 0
count_of_4 = 0
count_of_5 = 0
for i in range(n):
    mark = int(input('Введите оценку: '))
    if mark == 3:
        count_of_3 += 1
    elif mark == 4:
        count_of_4 += 1
    elif mark == 5:
        count_of_5 += 1
if count_of_3 > count_of_4 and count_of_3 > count_of_5:
    print('Больше всего троечников')
elif count_of_4 > count_of_3 and count_of_4 > count_of_5:
    print('Больше всего хорошистов')
else:
    print('Больше всего отличников')