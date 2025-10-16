import re

text = "abc_def ghi_jkl mno"
matches = re.findall(r'[a-z]+_[a-z]+', text)
print(matches)