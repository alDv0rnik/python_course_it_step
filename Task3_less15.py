"""
Реализовать функцию get_pairs(lst: List) -> List[Tuple], которая возвращает список из кортежей, содержащих пары элементов.
Пары следует формировать так, как показано в примере. Если в списке есть только один элемент, то вернуть None
"""


def get_pairs():
    lst = []

    def geting(lst_: list) -> list[tuple]:
        for i in range(len(lst_) - 1):
            c = (lst_[i], lst_[i + 1])
            lst.append(c)
        return lst

    if lst == None:
        return None
    else:
        return geting


get_ = get_pairs()
x = input().split()
print(get_(x))
