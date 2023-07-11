"""
Напишите функцию concat, которая будет принимать произвольное число строк и объединять их в одну
"""


def concat(lst: list):
    return ''.join(lst)


txt = input().split()
print(concat(txt))
