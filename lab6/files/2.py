import os

p = r"/Users/adelkikbai/Desktop/code/pp2"

def ch(path):
    if not os.path.exists(path):
        print("path doesn't exist")
        return
    else:
        print("path does exist")
        if os.access(path, os.R_OK):
            print("redable")
        else:
            print("doesn't redable")

        if os.access(path, os.W_OK):
            print("writable")
        else:
            print("doesn't writable")

        if os.access(path, os.X_OK):
            print('executable')
        else:
            print("doesn't executable")

ch(p)