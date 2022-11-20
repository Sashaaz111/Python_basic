def count_letters(num, letter):
    sum_num = 0
    sum_let = 0
    for i in text:
        if i == num:
            sum_num += 1
        elif i == letter:
            sum_let += 1
    print('Количество цифр', num, '=', sum_num)
    print('Количество букв', letter, '=', sum_let)

text = input('Введите текст: ')
num = input('Какую цифру ищем? ')
letter = input('Какую букву ищем? ')
count_letters(num, letter)