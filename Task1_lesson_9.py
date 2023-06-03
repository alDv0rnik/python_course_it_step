"""
Написать программу, которая на вход принимает целое число N. Вывести в консоль число Фибоначчи, равное N
"""

n = int(input())
fib1, fib2 = 1, 1

for i in range(-1, n):
    fib1, fib2 = fib2, fib1 + fib2

print(fib1, end=" ")
