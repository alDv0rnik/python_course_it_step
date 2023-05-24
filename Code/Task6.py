"""
Даны 4 числа a, b, c и d.
Одно из них отлично от оставшихся, равных друг другу. Необходимо вывести данное число.
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == b == c:
    print(d)
elif a == b == d:
    print(c)
elif b == d == c:
    print(a)
else:
    print(b)

