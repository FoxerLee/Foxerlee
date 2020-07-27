import os

path = 'assets'
files = os.listdir(path)


for file in files:
    print("![" + file + "](https://raw.githubusercontent.com/Foxerlee/Foxerlee/master/assets/" + file + ")")
