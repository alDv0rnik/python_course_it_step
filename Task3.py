#Пройтись по диапазону чисел от 0 до 100 и вывести только те из них,
# которые делятся на 3

a = 0
b = 100

while b >= a:
    if b % 3 == 0:
        print(b)
    b -= 1