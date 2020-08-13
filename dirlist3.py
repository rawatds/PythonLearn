import os
import pathlib

print("Printing files only in a directory...")

basepath = "mydir"

for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):       # OR    os.path.isfile(basepath + "/" +  entry)
        print(entry)

print()

for entry in os.scandir(basepath):
    if entry.is_file():
        print(entry.name)

print()

for entry in pathlib.Path(basepath).iterdir():
    if entry.is_file():
        print(entry.name)