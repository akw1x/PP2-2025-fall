def num(N):
    while N >= 0:
        yield N
        N -= 1

n = int(input())
for x in num(n):
    print(x)