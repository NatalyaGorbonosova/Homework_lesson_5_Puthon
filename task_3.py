#задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.
import re
def find_abv(list_word):
    list_except = []
    for word in list_word:
        if 'абв'  in word: list_except.append(word)
    return list_except
def delete_word(list_except, text):
    for word in list_except:
        new_text = re.sub(r'\b' + word + r'\b', '', text)
        text = new_text
    return new_text
try:
    mytext = 'Очень абвгд долго делала эту задачу, но рагабв регулярные вабврол вабв2 выражения прабв помогли абв!!! прабвыл ура!!!'
    
    list_word = re.split(r'\W+', mytext)
    print(list_word)
    new_list = find_abv(list_word)
    print(f'Список слов, которые надо удалить: \n {new_list}')
    print(delete_word(new_list, mytext))
except: print('Wrong')
            