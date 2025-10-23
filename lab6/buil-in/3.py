def pol(s):
    s = s.lower().replace(" ","")
    l = ''.join(reversed(s))
    return s == l

s = input()
print(pol(s))