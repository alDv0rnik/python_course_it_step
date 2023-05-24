"""Даны две различные клетки шахматного поля, каждая из которых задаётся двумя числами,
— координата по x, координата по y. Вывести 1,
если шахматный ферзь сможет перейти с первой клетки на вторую одним ходом, иначе вывести 0."""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')