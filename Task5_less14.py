"""
Напишите функцию factorial, которая принимает на вход одно неотрицательное число, и возвращает значение
факториала данного числа.
"""


def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n


print(factorial(4))
