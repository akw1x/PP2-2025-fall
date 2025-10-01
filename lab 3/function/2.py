def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

f = float(input())
c = fahrenheit_to_celsius(f)
print(f"{f} Fahrenheit is equal to {c} Celsius")