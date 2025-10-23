import os 

path = r"/Users/adelkikbai/Desktop/code/pp2"
def checker(path):
    if os.path.exists(path):
        print(os.path.basename(path))
        print(os.path.dirname(path))

checker(path)