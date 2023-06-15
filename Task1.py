"""
Создайте словарь из строки 'pythonist' следующим образом: в качестве ключей возьмите буквы строки, а значениями пусть
будут числа, соответствующие количеству вхождений данной буквы в строку.
"""
from collections import Counter
st = list('pythonist') # st = list(input())
dc = {}
for i in st:
    dc[i] = st.count(i)
print(dc)