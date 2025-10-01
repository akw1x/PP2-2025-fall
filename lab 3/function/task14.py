import math

def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_celsius(f):
    return (5/9) * (f - 32)

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None, None

def filter_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [num for num in numbers if is_prime(num)]

def sphere_volume(r):
    return (4/3) * math.pi * (r ** 3)