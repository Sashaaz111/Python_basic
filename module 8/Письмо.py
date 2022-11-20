letter_size = int(input('Введите размеры письма: '))
envelope = 12
count = 0
for i in range(letter_size, -1, -envelope):
    if letter_size > envelope:
        letter_size /= 2
        count += 2
print('Письмо надо сложить в', count, 'раза')

