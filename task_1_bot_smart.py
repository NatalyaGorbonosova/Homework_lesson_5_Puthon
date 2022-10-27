# задача 1. Создайте программу для игры с конфетами человек против умного бота.
from random import randint
def who_start():
    number = randint(1, 2)
    if number == 1: str = 'начинает человек'
    else: str = 'начинает бот'
    return str
def human_motion(candies):
    if candies <= 28 and candies != 0: 
            print('Победил человек!!!')
            num1=candies
    else:
        num1 = int(input(f'Человек делает ход. Сколько конфет возьмете? '))
        if num1 <= 28: 
            print(f'Человек взял: {num1} конфет')
        else:
            print('Вы взяли неправильное количество конфет, поэтому ход переходит к другому игроку. Пожалуйста не нарушайте правила!')
            num1 = 0
    return num1
def bot_motion(candies, num1):
    if candies <= 28 and candies != 0: 
        print('Победил бот!!!')
        num2 = candies
    elif candies == 0:
        print('Бот проиграл')
        num2 = 0
    else:
        num2 = 29 - num1
        print(f'Бот взял:{num2} конфет')
    return num2
try:
    first = who_start()
    print(f'Игру {first} !')
    if first == 'начинает бот':
        print('Бот взял 20 конфет. Осталось 1993 конфеты')
        count_candy = 2021 - 20
        while count_candy > 0:
            human = human_motion(count_candy)
            count_candy -= human
            bot = bot_motion(count_candy, human)
            count_candy -= bot
            print(f'Текущее количество конфет равно: {count_candy}')
    else:
        count_candy = 2021
        check = 0
        while count_candy > 0:
            human = human_motion(count_candy)
            count_candy -= human
            
            if check == 0 and human < 20:
                bot = 20 - human
                check = 1
            else: bot = bot_motion(count_candy, human)
            count_candy -= bot
            print(f'Текущее количество конфет равно: {count_candy}')
except: print('Можно брать от 1 до 28 кофет за один раз!!!')