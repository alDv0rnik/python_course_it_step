"""Перевести строку "it_step_courses" из snake case в camel case"""

a = "it_step_courses"
b = a.replace("_", "").replace("i","I",1).replace("s","S",1).replace("c","C",1)
print(b)
