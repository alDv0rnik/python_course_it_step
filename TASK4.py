#Для функции из любой задачи написать аннотацию, используя правила docstring (PEP 257)


def func(lst: list) -> list:
    """

    :param lst: List
    :return: Sorted List
    """
    return sorted(set(lst))


lst = input().split()
print(func(lst))
print(func.__doc__)
