"""
Создайте любую переменную строку и поместите туда любой текст. Сделайте так, чтобы все нечетные по порядку слева на
 право символы стали “_”, а все символы, местоположение которых четное и которые равны “a” - стали “b”.
"""
txt = input()
txt1 = "_"

for i in range(1, len(txt), 2):
    txt1 += txt[i] + "_"

txt1 = txt1.replace("a", "b")
print(txt1)
