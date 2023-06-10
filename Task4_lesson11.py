"""
Пусть есть число, где сумма всех цифр слева от середины равна сумме всех цифр справа. Такое число называется сбалансированным.
Если количество цифр в числе нечётное, то бери суммы слева и справа от средней цифры. Дано целое положительное число N. Если оно
является сбалансированным, то выведи 1, иначе 0.
"""

n1 = list(input())
n2 = list(map(int, n1))
if len(n2) % 2 == 0:
    num1 = []
    for i in range(int(len(n2) / 2)):
        num1.append(n2.pop(0))
    if sum(n2) == sum(num1):
        print(1)
    else:
        print(0)
elif len(n2) % 2 == 1:
    n2.pop(int(len(n2) / 2))
    num2 = []
    for i in range(int(len(n2) / 2)):
        num2.append(n2.pop(0))
    if sum(n2) == sum(num2):
        print(1)
    else:
        print(0)