"""
Реализовать функцию get_pairs(lst: List) -> List[Tuple], которая возвращает список из кортежей, содержащих пары
элементов. Пары следует формировать так, как показано в примере. Если в списке есть только один элемент, то вернуть None
"""
def get_pairs():
    l1 = []

    def geting(lst: list) -> list[tuple]:
        for i in range(len(lst) - 1):
            c = (lst[i], lst[i + 1])
            l1.append(c)
        return l1


    if l1 == None:
        return None
    else:
        return geting


ts = get_pairs()
lst = input().split()
print(ts(lst))