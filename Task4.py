"""
Реализовать функцию generate_squares(i: int) -> dict(int: int), которая принимает число в качестве аргумента и
возвращает словарь, где ключ - это число, а значение - квадрат этого числа.
"""
def dkt_gen():
    dk = {}
    count = 1


    def generate_squares(i: int):
        nonlocal count
        dk[count] = i ** 2
        count += 1
        return dk

    return generate_squares


gen = dkt_gen()
num = int(input())
print(gen(num))
print(gen(9))
print(gen(2))
print(gen(72))
