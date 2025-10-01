from itertools import permutations

def per(s):
    for perm in permutations(s):
        print(''.join(perm))

user_input = input("Enter a string: ")
per(user_input)