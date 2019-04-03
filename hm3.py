#1
"""
a = [i for i in range(2, 100)]
b = 0
for i in range(2, 10):
    for j in range(len(a)):
        if a[j] % i == 0:
            b += 1
    print(f'{i} - {b}')
    b = 0
"""
#2
"""
a = input().split(', ')
a = [int(a[i]) for i in range(len(a))]
b = [i for i in range(len(a)) if a[i] % 2 == 0]
print(b)
"""
#3
"""
a = input().split(', ')
a = [int(a[i]) for i in range(len(a))]
b = [i for i in range(len(a)) if a[i] == max(a) or a[i] == min(a)]
a[b[0]], a[b[1]] = a[b[1]], a[b[0]]
print(a)
"""
#4
"""
a = input().split(', ')
a = [int(a[i]) for i in range(len(a))]
b = list(set(a[i] for i in range(len(a)) if a.count(a[i]) == max([a.count(a[t]) for t in range(len(a))])))
print(b)
"""
#5
"""
a = input().split(', ')
a = [int(a[i]) for i in range(len(a))]
b = max(a[i] for i in range(len(a)) if a[i] < 0)
c = max(i for i in range(len(a)) if a[i] == b)
print(f'{b} {c}')
"""
#6
"""
a = input().split(', ')
a = [int(a[i]) for i in range(len(a))]
b = [i for i in range(len(a)) if a[i] == max(a) or a[i] == min(a)]
s = sum(a[min(b) + 1:max(b)])
print(s)
"""
#7
"""
a = input().split(', ')
a = [int(a[i]) for i in range(len(a))]
b = min(a)
r = max(a)
if a.count(b) == 1:
    for i in range(len(a)):
        if a[i] < r and a[i] > b:
            r = a[i]
else:
    r = b
print(f'{b} {r}')
"""
#8
"""
u = 0
m = int(input('Количество строк - '))
n = int(input('Количество столбцов - '))
a = [input().split(' ') for i in range(m)]
a = [[int(a[i][j]) for j in range(n)] for i in range(len(a))]
for i in range(m):
    a[i].append(sum(a[i]))
    for j in range(n + 1):
         print(a[i][j], end=' ')
         u += 1
         if u == n + 1:
             u = 0
             print()
"""
#9
"""
m = int(input('Количество строк - '))
n = int(input('Количество столбцов - '))
a = [input().split(' ') for i in range(m)]
b = [[int(a[i][j]) for i in range(m)] for j in range(n)]
x = [min(b[i]) for i in range(len(b))]
print(max(x))
"""