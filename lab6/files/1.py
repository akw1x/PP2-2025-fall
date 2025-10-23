import os 

path = r"/Users/adelkikbai/Desktop/code/pp2"
all = []

dir = []
fil = []
for (roots, dirs, files) in os.walk(path, topdown=True):
    dir.extend(dirs)
    fil.extend(files)
    all.extend(dirs)
    all.extend(files)

print(dir)
print(fil)
print(all)
