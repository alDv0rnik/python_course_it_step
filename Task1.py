"""
Перевести строку "it_step_courses" из shake case в camel case
"""

a = "it_step_courses"
print(a.replace('_', '').replace('i', 'I', 1).replace('s', 'S', 1).replace('c', 'S',1))