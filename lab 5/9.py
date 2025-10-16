import re

text = "InsertSpaceBeforeCapitalLetters"
result = re.sub(r'(?=[A-Z])', ' ', text).strip()
print(result)