"""
Дана строка в виде случайной последовательности чисел от 0 до 9. Требуется создать словарь,
который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве
значений – количество этих чисел в имеющейся последовательности. Программа должна возвратить словарь из 3-х
самых часто встречаемых чисел.
"""

from collections import Counter

number = list(input())

for i in range(len(number)):
    number[i] = int(number[i])
k = Counter(number)
print(dict(k.most_common(3)))
