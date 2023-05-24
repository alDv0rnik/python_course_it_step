"""
На вход дается любое число. Узнать скольки разрядов в числе - оно (1, 2, 3 или более значное), положительное или
отрицательное? Например, 25 — это двузначное положительное, а -345 это трехзначное отрицательное, а 2400 это 3х и более
значное положительное. 0 учитывать как отдельный вариант, а не как однозначное число
"""
num = int(float(input()))
if "-" in str(num) and int(len(str(abs(num)))) == 1:
    print("a negative single number")
elif int(len(str(abs(num)))) == 1:
    print("positive single number")
elif "-" in str(num) and int(len(str(abs(num)))) == 2:
    print("a negative two-digit number")
elif int(len(str(num))) == 2:
    print("positive two-digit number")
elif "-" in str(num) and int(len(str(abs(num)))) >= 3:
    print("a negative three or more digit number")
elif int(len(str(num))) >= 3:
    print("three or more digit number")
else:
    print("eror")

