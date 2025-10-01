def grams_to_ounces(grams):
    return 28.3495231 * grams

grams = float(input())
ounces = grams_to_ounces(grams)
print(f"{grams} grams is equal to {ounces} ounces")