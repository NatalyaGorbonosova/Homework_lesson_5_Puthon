# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
import re
def data_compression(str):
    list = []
    a = str[0]
    ind = 0
    while ind < len(str):
        count = 0
        for e in str:
            if e == a: count +=1
            else: break
        ind = str.index(a) + count
        list.append(f'{count}{a}') 
        if ind < len(str): a = str[ind]
        else: break
        str = str[count:len(str)]
        ind = 0
    new_str = ''
    for e in list:
        new_str += e 
    return new_str
def data_recovery(str):
    count_sim = ''
    new_str = ''
    for e in str:
        if e.isdigit():
            count_sim += e
        else:
            new_str += e * int(count_sim)
            count_sim = ''
    return new_str

try:
    initial_data = 'bbannnnnnnnwwwwwwwwwwwwwwwwww'
    with open('initial_data.txt', 'w') as data_start:
        data_start.write(initial_data)
    
    with open('compressed_data.txt', 'w') as data_compres:
        data_compres.write(data_compression(initial_data))
    data_start.close()
    str_compr = ''
    with open('compressed_data.txt', 'r') as data_compres:
        for line in data_compres:
            str_compr += line
    print(str_compr)
    data_compres.close()
    with open('recovered_data.txt', 'w') as data_recov:
        data_recov.write(data_recovery(str_compr))
    with open('recovered_data.txt', 'r') as data_recov:
        for line in data_recov:
            print(line)
    data_recov.close()
except: print('Wrong')