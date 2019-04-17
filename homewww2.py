#1
"""
b = 1
while b == 1:
    a = input("Введите выражение: ").split(' ')
    if a[1] == '0':
        b = 0
    else:
        if a[1] == '+':
            print(int(a[0]) + int(a[2]))
        elif a[1] == '-':
            print(int(a[0]) - int(a[2]))
        elif a[1] == '*':
            print(int(a[0]) * int(a[2]))
        elif a[1] == '/' and a[2] != '0':
            print(int(a[0]) / int(a[2]))
        else:
            print('Ошибка')
"""
#2
"""
a = input('Введите число: ')
c = 0
b = 0
for i in range(len(a)):
    if int(a[i]) % 2 == 0:
        b += 1
    else:
        c += 1
print(f"{b} {c}")
"""
#3
"""
def num(x):
    if not x:
        return
    print (x%10)
    num(x//10)
num(int(input('Введите число: ')))
"""
#4
"""
a = 1
b = int(input())
s = 0
while b > 0:
    a /= -2
    s += a
    b -= 1
print(s)
"""
#5
"""
for i in range(32, 128):
    print(chr(i), end=' ')
    if (i - 1) % 10 == 0:
        print()
print()
"""
#6
"""
import random
a = random.randint(0, 100)
p = 0
for i in range(10):
    b = int(input())
    if b > a:
        print('Больше')
    elif b < a:
        print('Меньше')
    elif b == a:
        print('Победа')
        p = 1
        break
if p == 0:
    print(f'Вы проиграли, правильно число было: {a}')
"""
#7
"""
a = int(input())
b = a
c = 1
y = 1
while b > 1:
    b -= 1
    y += 1
    c += y

if c == a*(a + 1) / 2:
    print('true')
else:
    print('false')
"""
#8
"""
a = input()
b = int(input())
c = input()
d = 0
for i in range(b):
    if a[i] == c:
        d += 1
print(d)
"""
#9
"""
a = input().split(' ')
m = 0

for i in range(len(a)):
    n = int(a[i])
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    if s > m:
        m = s
        i1 = i

print(f'{a[i1]} {m}')
"""