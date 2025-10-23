n = input().split()

data = tuple(int(x) if x.isdigit() else x for x in n)
print(all(data))