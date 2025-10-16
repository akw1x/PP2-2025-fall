import re

pattern = r'ab{2,3}'

strings = ["ab", "abb", "abbb", "abbbb", "a", "babb"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")
    else:
        print(f"No match: {s}")