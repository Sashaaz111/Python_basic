text = input('Введите текст: ')
position = 1
for i in text:
    if i == '*':
        print('Символ "*" стоит на позиции', position)
    else:
        position += 1
