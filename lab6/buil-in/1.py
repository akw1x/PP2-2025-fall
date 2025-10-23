from functools import reduce
from operator import mul

def ml(num):
    return reduce(mul, num)

n = input()
num = list(map(int,n.split()))

print(ml(num))