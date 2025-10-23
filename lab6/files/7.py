import os 

def cf(A, B):
    with open(A, 'r') as fr, open(B, 'w') as sc:
        sc.write(fr.read())

cf("A.txt", "B.txt")   