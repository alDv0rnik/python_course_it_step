"""
Напишите программу, которая считает количество символов в строке (игнорирует регистр)
"""
import collections

str = list(input().lower())
print(str)
dict = collections.Counter(str)
print(dict)