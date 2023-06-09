#ROT13 — это простой шифр, который заменяет каждую букву строки буквой,
# которая находится на 13 букв после неё в алфавите. Программа получает на вход строку,
# необходимо зашифровать её с помощью ROT13 и вывести результат.
# Используйте латинский алфавит



import string

n = 13
alpha = string.ascii_lowercase
text = "Hello world"
new_text = ""

for letter in text:
    if letter == " ":
        new_text += " "
    else:
        old_index = alpha.find(letter.lower())
        new_index = (old_index + n) % len(alpha)
        new_text += alpha[new_index]

print(text)
print(new_text)