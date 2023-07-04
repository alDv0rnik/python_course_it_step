"""
Для функции из любой задачи написать аннотацию, используя правила docstring (PEP 257)
"""
def add_2(num: int, /) -> int:
    """
    The function increases the number by 2
    :param num: int
    :return: int
    """
    return num + 2


num = int(input())
print(add_2(num))