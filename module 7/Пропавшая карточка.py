N = int(input('Введите кол-во карточек: '))
count = 0
for i in range(1, N + 1):
    count += i
for i in range(N - 1):
    num_card = int(input('Введите номер оставшейся карточки: '))
    count -= num_card
print('Номер пропавшей карточки:', count)