import os 

def df(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File '{path}' has been deleted successfully.")
        else:
            print(f"Cannot delete '{path}'.")
    else:
        print(f"'{path}' does not exist.")
        
df("D.txt")
