text = input('Введите зашифрованное сообщение: ')
count = 0
start = ''
end = ''
for i in text:
    if count % 2 == 0:
        start += i
    else:
        end = i + end
    count += 1
word = start + end
print('Расшифрованное собщение:', word)