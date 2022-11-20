text = input('Введите строку: ')
count = 0
max_count = 0
for i in text:
    if i != ' ':
        count += 1
    else:
        count = 0
    if count > max_count:
        max_count = count
print('Самое длинное слово, букв:', max_count)
