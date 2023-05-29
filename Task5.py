"""
Дано натуральное число N. Если оно является простым, то следует вывести 1, иначе - 0. Простым называется число, которое
 делится без остатка на себя и 1.
"""
num = input()
if float(num) % 1 != 0:
    print(0)
elif float(num) % 1 == 0 and float(num) % float(num) == 0:
    print(1)
else:
    print("error")
