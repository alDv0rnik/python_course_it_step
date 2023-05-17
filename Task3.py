"""Требуется определить индексы первого и последнего вхождения буквы в строке. Гарантируется, что буква присутствует в
последовательности"""

word = input().lower()
letter = "i"

print(f"Left index {word.find(letter)}\nRight index {word.rindex(letter)}\nNumber of indices {len(word)}")
