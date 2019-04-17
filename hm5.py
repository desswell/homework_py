"""
from collections import namedtuple
# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
enterprises = []

count_ent = int(input('Введите кол-во предприятий: '))

Enterprise = namedtuple('Enterprise', 'name qua_1 qua_2 qua_3 qua_4')

sum_1 = 0

for i in range(count_ent):
    ent = [input('Введите имя предприятия: '), int(input('Введите прибыль за первый квартал: ')), int(input('Введите прибыль за второй квартал: ')), int(input('Введите прибыль за третий квартал: ')), int(input('Введите прибыль за четвертый квартал: '))]
    enterprises.append(Enterprise._make(ent))
    sum_1 += enterprises[i].qua_1 + enterprises[i].qua_2 + enterprises[i].qua_3 + enterprises[i].qua_4

print(f'Средняя прибыль {sum_1 / count_ent}')

print('Предприятия, чья прибыль выше среднего: ')

for i in range(count_ent):
    if enterprises[i].qua_1 + enterprises[i].qua_2 + enterprises[i].qua_3 + enterprises[i].qua_4 > sum_1 / count_ent:
        print(enterprises[i].name)

print('Предприятия, чья прибыль ниже среднего: ')

for i in range(count_ent):
    if enterprises[i].qua_1 + enterprises[i].qua_2 + enterprises[i].qua_3 + enterprises[i].qua_4 < sum_1 / count_ent:
        print(enterprises[i].name)
"""
"""
# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
SCALE = 16

a_1 = list(input('Введите число A: '))
b_1 = list(input('Введите число B: '))

dict_hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
dict_hex_val = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}

copy_a = a_1[:]
copy_b = b_1[:]

def sum_16(a, b):
    if len(a) > len(b):
        a, b = b, a

    next_i = 0
    str_sum = ''

    while len(b) != 0:
        if len(a) == 0 and len(b) != 0:
            sum_1 = (dict_hex[b[len(b) - 1]] + next_i) % SCALE
            next_i = (dict_hex[b[len(b) - 1]] + next_i) // SCALE
            str_sum += dict_hex_val[str(sum_1)]

            del b[len(b) - 1]
            if len(b) == 0:
                str_sum += dict_hex_val[str(next_i)] if next_i != 0 else ''
                str_sum = list((str_sum))[::-1]

            continue


        sum_1 = (dict_hex[a[len(a) - 1]] + dict_hex[b[len(b) - 1]] + next_i) % SCALE
        next_i = (dict_hex[a[len(a) - 1]] + dict_hex[b[len(b) - 1]] + next_i) // SCALE
        str_sum += dict_hex_val[str(sum_1)]

        del a[len(a) - 1]
        del b[len(b) - 1]

        if len(b) == 0:
            str_sum += dict_hex_val[str(next_i)] if next_i != 0 else ''

            str_sum = list((str_sum))[::-1]

    return str_sum

print(''.join(sum_16(a_1, b_1)))


a_2, b_2 = copy_a, copy_b

str_mult_1 = ['0']
str_mult = ['0']

if len(a_2) > len(b_2):
    a_2, b_2 = b_2, a_2

counter_i = 0

for i in range(0, len(a_2)):
    str_mult = ['0']
    for _ in range(dict_hex[a_2[len(a_2) - i - 1]]):
        str_mult = sum_16(str_mult[:], b_2[:])

    for _ in range(counter_i):
        str_mult += ['0']

    str_mult_1 = sum_16(str_mult_1[:], str_mult[:])
    counter_i += 1

print(''.join(str_mult_1))
"""