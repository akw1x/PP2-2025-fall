def gen_sqr(N):
    for i in range (N+1):
        yield i ** 2

n = int(input())
for x in gen_sqr(n):
    print(x)