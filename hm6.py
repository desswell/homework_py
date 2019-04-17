# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
import struct
import sys
import ctypes
def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                show_size(y, level + 1)

        elif not isinstance(x, str):
            for y in x:
                show_size(y, level + 1)

#1
"""
a = input().split(', ')
a = [int(a[i]) for i in range(len(a))]
b = list(set(a[i] for i in range(len(a)) if a.count(a[i]) == max([a.count(a[t]) for t in range(len(a))])))
print(*b)
show_size(b)
"""
#2
"""
a = input().split(', ')
a = [int(a[i]) for i in range(len(a))]
b = [i for i in range(len(a)) if a[i] == max(a) or a[i] == min(a)]
s = sum(a[min(b) + 1:max(b)])
print(s)
show_size(b)
"""
#Программы написанны очень эффективно