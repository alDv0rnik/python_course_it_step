"""
Пусть есть число, где сумма всех цифр слева от середины равна сумме всех цифр справа.
Такое число называется сбалансированным. Если количество цифр в числе нечётное, то бери суммы слева и справа от средней
 цифры. Дано целое положительное число N. Если оно является сбалансированным, то выведи 1, иначе 0.
"""
num0 = list(input())
num = list(map(int, num0))
if len(num) % 2 == 0:
    num1 = []
    for i in range(int(len(num) / 2)):
        num1.append(num.pop(0))
    if sum(num) == sum(num1):
        print(1)
    else:
        print(0)
elif len(num) % 2 == 1:
    num.pop(int(len(num) / 2))
    num2 = []
    for i in range(int(len(num) / 2)):
        num2.append(num.pop(0))
    if sum(num) == sum(num2):
        print(1)
    else:
        print(0)
