#Напишите функцию func, которая принимает список и возвращает его уникальную копию в
# исходном порядке, то есть каждый элемент входит в список ровно один раз.
# Элементы в списке принимают значения от 0 до 100.

Input: [1, 15, 35, 4, 1, 15]
Output: [1, 15, 35, 4]


def func(lst: list) -> list:
    return sorted(set(lst))


lst = input().split()
print(func(lst))