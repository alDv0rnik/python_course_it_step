"""
Написать программу, которая определяет, что за зверь находится перед нами. Если зверь говорит “Meow”, то это кошка,
 если “Bark”, то это собака, а если что-то другое, то это “Неизвестный зверь”
"""
animal = input()
if animal.lower() == "meow":
    print("I's a cat")
elif animal.lower() == "bark":
    print("I's a dog")
else:
    print("unknown animal")
