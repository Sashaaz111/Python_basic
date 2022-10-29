text = input('Введите строку: ')
count = 0
max_count = 0
for i in text:
    if i == 's':
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0
print('Самая длинная последовательность:', max_count)
