def even_gen(N):
    for i in range (N+1):
        if i % 2 == 0:
            yield i

n = int(input())
print(",".join(str(x) for x in even_gen(n)))