"""
Пусть число, где все соседние цифры в нём отличаются на 1, называется прыгающим.
Программа получает на вход целое положительное число N, если оно является прыгающим, то выведи 1, иначе 0.
"""
num = input("way 1:")
a = []
if "-" in num:
    print(0)
else:
    for i in range(len(num)):
        if len(num) == i + 1:
            break
        if int(num[i]) == int(num[i+1]) + 1 or int(num[i]) == int(num[i+1]) - 1:
            a.append(1)
            continue
        if int(num[i]) == int(num[i-1 or i+1]) + 1 or int(num[i]) == int(num[i-1 or i+1]) - 1:
            a.append(1)
        else:
            a.append(0)
if 0 in a:
    print(0)
else:
    print(1)

num1 = input("way 2:")
a = 0
if "-" in num1:
    print(0)
else:
    for i in range(len(num1) - 1):
        num1 = list(num1)
        b = int(num1.pop(0))
        if b == int(num1[0]) + 1 or b == int(num1[0]) - 1:
            a = 1
        else:
            a = 0
            break
print(a)