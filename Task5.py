"""
Реализовать функцию split_by_index(s: str, indexes: List[int]) -> List[str], которая делит строку s с помощью индексов,
указанных в indexes. Неправильные индексы должны быть проигнорированы.
"""
def split_by_index(s: str, indexes: list[int]) -> list[str]:
    lst = []
    a = 0
    for i in indexs:
        lst.append(s[a:i])
        a = i
    return lst


s = "pythoniscool,isn'tit?"
indexs = [6, 8, 12, 13, 18]
print(split_by_index(s, indexs))