import re

pattern = r'ab*'

strings = ["a", "ab", "abb", "ac", "b", "ba"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")
    else:
        print(f"No match: {s}")