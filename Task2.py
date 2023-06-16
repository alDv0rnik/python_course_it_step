#Напишите программу, которая считает количество символов в строке (игнорирует регистр)
#Для решения задачи можно использовать класс Counter из модуля collections


from collections import Counter

string = 'Oh, it is python'.lower()
counter_string = Counter(string)
print(counter_string)
