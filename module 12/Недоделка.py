import random

def rock_paper_scissors():
    print('Запустилась игра: Камень, ножницы, бумага')
    my_choice = input('Выберите одно: "Камень", "Ножницы", "Бумага": ')
    bot_choice = random.choice(['Камень', 'Ножницы', 'Бумага'])
    print('Бот выбрал:', bot_choice)
    if my_choice == bot_choice:
        print('Ничья!')
    elif my_choice == 'Камень' and bot_choice == 'Ножницы':
        print('Камень бъет ножницы! Вы выиграли')
    elif my_choice == 'Камень' and bot_choice == 'Бумага':
        print('Бумага кроет камень! Вы проиграли')
    elif my_choice == 'Ножницы' and bot_choice == 'Бумага':
        print('Ножницы режут бумагу! Вы выиграли')
    elif my_choice == 'Ножницы' and bot_choice == 'Камень':
        print('Камень бъет ножницы! Вы проиграли')
    elif my_choice == 'Бумага' and bot_choice == 'Камень':
        print('Бумага кроет камень! Вы выиграли')
    elif my_choice == 'Бумага' and bot_choice == 'Ножницы':
        print('Ножницы режут бумагу! Вы проиграли')
    print('Хотите сыграть ещё раз?')
    ans = input('Ответ: ')
    if ans == 'Да' or ans == 'да' or ans == 'ДА':
        print('Запускаю игру...')
        rock_paper_scissors()
    elif ans == 'Нет' or ans == 'нет' or ans == 'НЕТ':
        print('Выход в главное меню...')
        mainMenu()

def guess_the_number():
    print('Запустилась игра: Угадай число от 1 до 10')
    num = random.randint(0, 10)
    answer = int(input('Введите число: '))
    while num != answer:
        print('Не угадали! Попробуйте ещё раз.')
        answer = int(input('Введите число: '))
    print('Поздравляю! Вы угадали.')
    print('Хотите сыграть ещё раз?')
    ans = input('Ответ: ')
    if ans == 'Да' or ans == 'да':
        print('Запускаю игру...')
        guess_the_number()
    elif ans == 'Нет' or ans == 'нет':
        print('Выход в главное меню...')
        mainMenu()


def mainMenu():
    varient = int(input('Выберите игру. 1 - Камень, ножницы бумага. 2 - Угадай число: '))
    if varient == 1:
        print('Запускаю игру...')
        rock_paper_scissors()
    elif varient == 2:
        print('Запускаю игру...')
        guess_the_number()
    else:
        print('Неверный ввод')
        mainMenu()

mainMenu()