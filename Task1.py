"""Перевести строку "it_step_courses" из shake case в camel case"""
txt = "it_step_courses"
txt_ = txt.replace("_", '').replace("i","I",1).replace("s","S",1).replace("c","C",1)

print(txt_)
