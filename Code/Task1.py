"""
Даны 3  целых числа a, b и c. Найти и вывести количество отрицательных.
Для ввода чисел использовать соответствующую функцию
"""
a = int(input())
b = int(input())
c = int(input())
count = 0
if a < 0:
    count += 1
if b < 0:
    count += 1
if c < 0:
    count += 1
print(count)
