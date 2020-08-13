import fnmatch 
import os
import glob


dir = "mydir"

for filename in os.listdir(dir):
    if filename.endswith(".txt"):
        print(filename)

print()

for filename in os.listdir(dir):
    if fnmatch.fnmatch(filename, "*.txt"):
        print(filename)

print()

for filename in os.listdir(dir):
    if fnmatch.fnmatch(filename, "*.txt"):
        print(filename)

print()
print(glob.glob("mydir/*.txt"))