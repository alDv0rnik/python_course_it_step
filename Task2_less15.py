"""
Напишите фунцкию to_percent(num: float), которая будет принимать вещественное число и представлять его в виде процентов.Так,
например, 0.1 это 10%, а 1.052 это 105.2%. Пускай функция будет принимать один необязательный параметрround_digits.
Который будет указывать на количество цифр после запятой в числе процентов, при этом незначащие нули нужноопускать. Если он не указан,
пускай ваша функция округляет результат до целого процента.
"""


def to_percent(x: float):
    return f'{x * 100}%'


n = float(input())
print(to_percent(n))