#1
a = int(input())
while a > 0:
        print(a%10, ' ')
        a = a // 10

#2
a = int(input())
b = int(input())

c = a
a = b
b = c

print (a, ' ', b)

#3
a = int(input())

if a >= 18:
        print('Доступ разрешен')
else:
        print('Извините, пользование данным ресурсом только с 18 лет')

