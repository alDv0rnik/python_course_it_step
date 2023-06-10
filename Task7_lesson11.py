"""
ROT13 — это простой шифр, который заменяет каждую букву строки буквой, которая находится на 13 букв после неё в алфавите.
Программа получает на вход строку, необходимо зашифровать её с помощью ROT13 и вывести результат. Используйте латинский алфавит
"""

import string
st = input()
n = 13
st2 = ""
alpha = string.ascii_letters + string.digits + string.punctuation

for i in st:
    if i == " ":
        st2 += " "
    else:
        old_index = alpha.find(i)
        new_index = (old_index + n) % len(alpha)
        st2 += alpha[new_index]

print(st2)
