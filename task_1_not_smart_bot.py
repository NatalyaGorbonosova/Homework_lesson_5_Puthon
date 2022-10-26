 #задача 1. Создайте программу для игры с конфетами бот против бота (оба без интеллекта).
from random import randint
try:
    number = randint(1, 2)
    print(f'Начинает игрок номер {number}')
    count_candy = 2021
    while count_candy >= 0:
        if count_candy <= 28: 
            print('Победил первый игрок!!!')
            count_candy = 0
            break
        num1 = randint(1, 28)
        print(f'Первый игрок взял: {num1} конфет')
        if num1 <= 28 and num1 > 0: 
            count_candy -= num1
        else: print('Вы взяли неправильное количество конфет, поэтому ход переходит к другому игроку. Пожалуйста не нарушайте правила!')
        if count_candy <= 28: 
            print('Победил второй игрок!!!')
            count_candy = 0
            break
        num2 = randint(1, 28)
        print(f'Второй игрок взял: {num2} конфет')
        if num2 <= 28 and num2 >0:
            count_candy -= num2
        else: print('Вы взяли неправильное количество конфет, поэтому ход переходит к другому игроку. Пожалуйста не нарушайте правила!')
        print(f'Текущее количество конфет равно: {count_candy}')
except: print('Можно брать от 1 до 28 кофет за один раз')