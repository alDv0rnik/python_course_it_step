"""
Создать список, состоящий из N элементов, которые указываются функцией ввода данных. Первым вводом указать размер списка
(N), далее — элементы списка.
Найди количество пар элементов, равных друг другу. Любые 2 элемента, равные друг другу, создают 1
пару, например: 5 5 5 5 5 — 10 пар.
"""
lst = list(input())
numbs = []
for i in range(len(lst)):
    for j in range(len(lst)):
        if i == j:
            continue
        if None == lst[j]:
            continue
        if None == lst[i]:
            break
        if lst[i] == lst[j]:
            numbs.append(lst[i])
    lst[i] = None
print(numbs, " - ", len(numbs), "pairs")
