"""
Написать программу, которая на вход принимает целое число N. Вывести в консоль число Фибоначчи, равное N
"""
num = int(input())
num1, num2 = 1, 1
num3 = 1

for i in range(num):
    num2, num1 = num1 + num2, num2;
    if int(num2 < num):
        num3 +=1
    elif int(num2 > num):
        break

print(num3)
