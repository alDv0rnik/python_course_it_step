"""
Напишите программу, которая считает количество символов в строке (игнорирует регистр) Для решения задачи можно
использовать класс Counter из модуля collections
(https://www.digitalocean.com/community/tutorials/python-counter-python-collections-counter )
"""
from collections import Counter
txt = input('Enter text: ').lower()
print(dict(Counter(txt)))