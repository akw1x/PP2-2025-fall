def ws(el):
    with open("ex.txt", 'w') as f:
        for i in el:
            f.write(str(i) + '\n')
        f.close()

n = input().split()

ws(n)