"""
Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом, чтобы элементы первого списка были
ключами, а элементы второго — соответственно значениями нашего словаря.
"""
strt = int(input('Enter Dictionary Size: '))
lst1 = []
lst2 = []
dct = {}
for key in range(strt):
    lst1.append(input(f'Enter Dictionary Keys ({key + 1}/{strt}):\n'))
for valu in range(strt):
    lst2.append(input(f'Enter Key Value ({lst1[valu]}):\n'))
for i in range(strt):
    dct[lst1[i]] = int(lst2[i])
print(dct)