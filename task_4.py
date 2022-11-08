# задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму.
def equation_standart(equat):   #Приводит уравнение к стандартному виду
    standart = equat.replace(" ", '')
    standart1 = standart.replace('*', '')
    return standart1
def polinom_ratio(polinom):
    i = 0
    j = 0
    n = 0
    pol_ratio = []
    while i < len(polinom) - 1:
        if polinom[i] == 'x' and polinom[i+1] == '^':
            if i != 0: 
                if polinom[i-1] != '-':
                    k = int(polinom[j: i])
                else: k = -1
                d = int(polinom[i+2])
                j = i + 3
                i = i + 3
                pol_ratio.append((k, d))
                n = i
            else:
                k = 1
                d = int(polinom[i+2])
                pol_ratio.append((k, d))
                j = i + 3
                i = i + 3
                n = i
        else: i = i +1
    end_of_pol = polinom[n: len(polinom)]
    ind_deg_1 = -1
    i = 0
    if end_of_pol.find('x') == -1: pol_ratio.append((int(end_of_pol), 0))
    else:
        if len(end_of_pol) != 0:
            while i < len(end_of_pol) - 1:
                if end_of_pol[i] == 'x' and i != 0:
                    ind_deg_1 = i
                    if end_of_pol[i-1] == '-': pol_ratio.append((-1, 1))
                    elif end_of_pol[i-1] == '+': pol_ratio.append((1, 1))
                    else:
                        k = int(end_of_pol[0:i])
                        pol_ratio.append((k, 1))
                elif end_of_pol[i] == 'x' and i == 0: 
                    pol_ratio.append((1, 1))
                    ind_deg_1 = i
                i = i + 1
        if ind_deg_1 >= 0:
            end_of_pol = end_of_pol[i-1:len(end_of_pol)]
            if len(end_of_pol) > 0: pol_ratio.append((int(end_of_pol), 0))
    return pol_ratio
def sort_list(list):
    for k in range(len(list)-1):
        pos_min = 0
        for i in range(len(list)-k):
            if list[i] < list[pos_min]:
                pos_min = i
        temp = list[pos_min]
        list[pos_min] = list[len(list)-1-k]
        list[len(list)-1-k] = temp
    return list
def sum_polinom(pol_1, pol_2, all_degree):
    sum_pol = ''
    for degree in all_degree:
        for i in range(len(pol_1)):
            if pol_1[i][1] == degree: 
                a = pol_1[i][0]
                break
            else: a = 0
        for i in range(len(pol_2)):
            if pol_2[i][1] == degree: 
                b = pol_2[i][0]
                break
            else: b = 0
        if degree > 1:
            if a + b > 0: sum_pol = sum_pol + f'+{a + b}*x^{degree}'
            elif a + b < 0: sum_pol = sum_pol + f'{a + b}*x^{degree}'
        elif degree == 1:
            if a + b > 0: sum_pol = sum_pol + f'+{a + b}*x'
            elif a + b < 0: sum_pol = sum_pol + f'{a + b}*x'
        elif degree == 0:
            if a + b > 0: sum_pol = sum_pol + f'+{a + b}'
            elif a + b < 0: sum_pol = sum_pol + f'{a + b}'
    return sum_pol
try:
    polinom_1 = equation_standart(input('Введите первый многочлен: ')) 
    polinom_2 = equation_standart(input('Введите второй многочлен: ')) 
    ratio_pol_1 = polinom_ratio(polinom_1)
    ratio_pol_2 = polinom_ratio(polinom_2)
    all_degree = []
    for i in range(len(ratio_pol_1)):
        all_degree.append(ratio_pol_1[i][1])
    for i in range(len(ratio_pol_2)):
        if ratio_pol_2[i][1] not in all_degree:
            all_degree.append(ratio_pol_2[i][1])
    all_degree = sort_list(all_degree)
    print(sum_polinom(ratio_pol_1, ratio_pol_2, all_degree))

except: print('Что-то пошло не так')