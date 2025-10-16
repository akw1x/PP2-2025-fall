import re

text = "SplitThisStringAtUppercase"
result = re.split(r'(?=[A-Z])', text)
print(result)