word_count = 0
for i in range(10):
    word = input('')
    if word == 'Карамба' or word == 'карамба':
        word_count += 1
print('Совпадающих слов:', word_count)