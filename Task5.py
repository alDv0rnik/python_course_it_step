"""
Даны две различные клетки шахматного поля, каждая из которых задаётся двумя числами, — координата по x, координата по y.
 Вывести 1, если шахматный конь сможет перейти с первой клетки на вторую одним ходом, иначе вывести 0
"""
x1 = int(input("enter x "))
y1 = int(input("enter y "))
x2 = int(input("enter x "))
y2 = int(input("enter y "))

if (x1 - 1 == x2 or x1 + 1 == x2) and (y1 - 2 == y2 or y1 + 2 == y2):
    print(bool(1))
elif (y1 - 1 == y2 or y1 + 1 == y2) and (x1 - 2 == x2 or x1 + 2 == x2):
    print(bool(1))
else:
    print(bool(0))
