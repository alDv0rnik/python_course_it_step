"""
Напишите функцию increase_g, которая будет возвращать результат выполнения функции g
увеличенный на 1. Т.е. если функция g() возвращает 1, то ваша функция в таком случае будет возвращать 2.
"""


def increase_g(x: int):
    y = g(x)
    return y + 1


def g(x: int) -> int:
    return x


i = int(input("Number?: "))
print(g(i))
print(increase_g(i))
