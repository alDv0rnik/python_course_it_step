"""Написать программу, которая определяет каким является число - четным или нечетным.
 Если остаток от деления на 2 не равен 0, то это нечетное число (вывести на консоль 0),
 а если равен - то четное (вывести на консоль 1). При решении использовать тернарный оператор"""
a = int(input())
if a % 2 == 0:
    print('Четное число')
else:
    print(' Не четное число')
