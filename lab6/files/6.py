import os 
import string 

def gen():
    for l in string.ascii_uppercase:
        fn = f"{l}.txt"

        with open(fn, "w") as file:
            file.write(f"This is {fn}\n")

gen()