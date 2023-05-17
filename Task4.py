"""На основании предоставленного отрывка текста определить наиболее часто встречаемый символ в ней.
Пробелы нужно игнорировать (не учитывать при подсчете)."""
from collections import Counter

text = """\
The Python ord() function converts a character into an integer that represents the Unicode code of the character.
Similarly, the chr() function converts a Unicode code character into the corresponding string.
"""
st = text.replace(' ','')
st1 = Counter(st)
st2 = st1.most_common(1)[0]

print(f"""The most frequently occurring character - "{st2[0]}"\nThe number of repetitions - "{st2[-1]}" """)
