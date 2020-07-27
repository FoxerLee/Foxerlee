import os

path = 'assets'
files = os.listdir(path)


for file in files:
    print("![" + file + "](assets/" + file + ")")
