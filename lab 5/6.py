import re

text = "Python, Java. C++ Go"
result = re.sub(r'[ ,.]', ':', text)
print(result)