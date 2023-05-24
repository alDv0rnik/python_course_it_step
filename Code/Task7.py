"""
Напишите программу, которая прочитает 3 числа и выведет максимум из них троих.
"""

a, b, c = int(input()), int(input()), int(input())

max = a
if b > max:
    max = b
if c > max:
    max = c
print(max)