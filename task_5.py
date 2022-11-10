# задача 5 необязательная Дан список чисел. Создайте список, в который попадают числа, описывающие максимальную 
# возрастающую последовательность. Порядок элементов менять нельзя.
import re
def fill_sequence():
    list = input('Введите числа через запятую: ')
    list_el = re.split(r'\W+', list)
    list_num = []
    for e in list_el:
        list_num.append(int(e))
    return list_num
def min_element(list):
    min = list[0]
    for el in list:
        if el < min: min = el
    return min
def next_element(element, list):
    for el in list:
        if el == element + 1:
            return el
def list_of_sequence(list):
    seq_list = []
    while len(list) > 0:
        member_list = []
        start_el = min_element(list)
        while start_el in list:
            member_list.append(start_el)
            list.remove(start_el)
            if next_element(start_el, list) is not None:
                start_el = next_element(start_el, list)
                
        seq_list.append(member_list)
    return seq_list
def max_sequence(list_of_seq):
    max_seq = list_of_seq[0]
    for i in range(len(list_of_seq)):
        
        if len(list_of_seq[i]) > len(max_seq): max_seq = list_of_seq[i]  
    return max_seq       
try:
    sequence = fill_sequence()
    print(sequence)
    list_seq = list_of_sequence(sequence)
    max_len = max_sequence(list_seq)
    print(f'Максимально возрастающая последовательность: [{max_len[0]}, {max_len[-1]}]')
except: print('Something wrong')