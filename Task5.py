"""
Напишите функцию factorial, которая принимает на вход одно неотрицательное число, и возвращает значение
факториала данного числа.
"""
import math

def factorial(n):
    if n > 1:
        return math.factorial(n)
    else:
        print("None")

print(factorial(int(input())))
