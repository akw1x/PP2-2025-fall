import re

pattern = r'a.*b$'
strings = ["a123b", "acb", "ab", "abc", "a_b", "abbc"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")
    else:
        print(f"No match: {s}")