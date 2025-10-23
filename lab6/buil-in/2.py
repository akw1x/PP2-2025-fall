def count(s):
    a = sum(1 for char in s if char.isupper())
    b = sum(1 for char in s if char.islower())
    return a, b


s = input()
up, low = count(s)

print("Заглавные буквы:", up)
print("Строчные буквы:", low)