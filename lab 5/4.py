import re

text = "Python Java C CPP GoLang"
matches = re.findall(r'[A-Z][a-z]+', text)
print(matches)