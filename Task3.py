"""
Даны 2 списка строк A1 и A2. Создай список, состоящий из строк списка A1,
которые являются подстроками строк из A2.
"""
lst1 = input("Set text1: ").split()
print(" ".join(lst1))
lst2 = input("Set text2: ").split()
lst3 = []
for i in range(len(lst1)):
    for j in range(len(lst2)):
        if lst2[j] in lst1[i]:
            lst3.append(lst1[i])
print("Text: ",lst3)
