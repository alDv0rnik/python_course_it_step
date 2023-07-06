"""
Напишите функцию concat, которая будет принимать произвольное число строк и объединять их в одну
"""
def concat(lst: list) -> str:
    return ''.join(lst)


text = input().split()
print(concat(text))