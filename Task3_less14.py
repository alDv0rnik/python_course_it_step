"""
Напишите функцию func, которая принимает список и возвращает его уникальную копию в исходном порядке,
то есть каждый элемент входит в список ровно один раз. Элементы в списке принимают значения от 0 до 100.
"""
"""
Для функции из любой задачи написать аннотацию, используя правила docstring (PEP 257)
"""


num = list(map(int, input().split()))


def get_unique_objects(num):
    """
    Accepts a list and returns a list
    with unique elements
    :param num: list
    :return: list
    """
    list_unique = []
    unq = set(num)
    for number in unq:
        list_unique.append(number)

    return list_unique


print(get_unique_objects(num))
