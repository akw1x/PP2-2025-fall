import math

def sphere_volume(r):
    return (4/3) * math.pi * (r ** 3)

# пример использования
radius = float(input())
print(f"Volume of the sphere with radius {radius} is {sphere_volume(radius)}")