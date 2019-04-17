"""
#coding utf-8
import cProfile
# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.

def row_of_num(n):
    sum_1 = 0

    list_1 = [i for i in range(1, n + 1)]

    for i in list_1:
        sum_1 += i

    return sum_1

# 1    0.000    0.000    0.000    0.000 less04_task01.py:5(row_of_num)  100 loops, best of 3: 58.7 usec per loop       - 1000
# 1    0.000    0.000    0.001    0.001 less04_task01.py:5(row_of_num)  100 loops, best of 3: 676 usec per loop        - 10000
# 1    0.003    0.003    0.008    0.008 less04_task01.py:5(row_of_num)  100 loops, best of 3: 8.17 msec per loop       - 100000
"""
"""
#coding utf-8
import cProfile
# Написать два алгоритма нахождения i-го по счёту простого числа.


def prime(n):

    lst=[2]
    i = 3
    count_of_num = 1

    while count_of_num < n:
        if (i > 10) and (i % 10 == 5):
            i += 2
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                count_of_num += 1
                i += 2
                break
            if (i % j == 0):
                i += 2
                break
        else:
            lst.append(i)
            i += 2
            count_of_num += 1
    return int(''.join(map(str, lst[-1:])))

# 1    0.000    0.000    0.000    0.000 less04_task01.py:8(prime)   100 loops, best of 3: 133 usec per loop      - 100
# 1    0.082    0.082    0.083    0.083 less04_task01.py:5(prime)   100 loops, best of 3: 78.5 msec per loop     - 10000
# 1    2.083    2.083    2.090    2.090 less04_task01.py:9(prime)   100 loops, best of 3: 2.11 sec per loop      - 100000




def sieve_num(n):

    sieve = [i for i in range(n)]

    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2

            while j < n:
                sieve[j] = 0
                j += i

    return int(''.join(map(str, [i for i in sieve if i != 0][-1:])))

# 1    0.000    0.000    0.000    0.000 less04_task01.py:35(sieve_num)  100 loops, best of 3: 18.3 usec per loop      - 100
# 1    0.002    0.002    0.003    0.003 less04_task01.py:32(sieve_num)  100 loops, best of 3: 2.7 msec per loop       - 10000
# 1    0.026    0.026    0.035    0.035 less04_task01.py:37(sieve_num)  100 loops, best of 3: 32.1 msec per loop      - 100000

def main():
    count_n = int(input("Введите n: "))
    print(f'Индексу n соответствует число {prime(count_n)}')

    # print(sieve_num(count_n))
"""