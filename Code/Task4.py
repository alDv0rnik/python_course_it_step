"""
Дано целое трёхзначное число a. Вывеcти количество чётных цифр в данном числе.
"""
# number = int(input())
#
# a = number % 10
# b = (number // 10) % 10
# c = number // 100
# count = 0
#
# if a % 2 == 0 and not a == 0:
#     count += 1
# if b % 2 == 0 and not b == 0:
#     count += 1
# if c % 2 == 0 and not c == 0:
#     count += 1
# print(count)


number = input()

a = int(number[0])
b = int(number[1])
c = int(number[2])
count = 0

if a % 2 == 0 and not a == 0:
    count += 1
if b % 2 == 0 and not b == 0:
    count += 1
if c % 2 == 0 and not c == 0:
    count += 1
print(count)