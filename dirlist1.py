import os
from pathlib import Path

print("*** Listting files and directories using 3 methods")

l = os.listdir("mydir/")

#print(type(l))
print(l)

print('------------------------')

files = os.scandir("mydir")
#print(type(files))
print(files)

for f in files:
    print(f.name)

print('------------------------')

entries = Path("mydir")
for entry in entries.iterdir():
    print(entry.name)
    #print(type(entry))

