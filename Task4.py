"""
Дано натуральное число N. Используя операции // и %, следует перевернуть данное число.
"""
num = input("Set number 1. ")
num1 = ""

for i in range(len(str(num))):
    num2 = int(-i - 1);
    num1 += num[num2]
print("Reverse number 1. ", num1)



num3 = int(input("Set number 2. "))
num4 = ""
num5 = ""

for i in range(len(str(num3))):
    num4 = str(int(num3 % 10));
    num3 = num3 / 10;
    num5 = num5 + num4

print("Reverse number 2. ", num5)