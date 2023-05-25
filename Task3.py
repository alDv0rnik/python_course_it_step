"""
Требуется определить индексы первого и последнего вхождения буквы в строке. Гарантируется, что буква присутствует в последовательности
"""

text = input().lower()
letter = input('letter: ')
print(f"Left index {text. find(letter)}\nRight index {text.rindex(letter)}")