# Tree walking

import os

for dirpath, dirname, files in os.walk("mydir"):
    print(dirpath, " : ", dirname, " : ", files)

def printdirandfile(dirname):
    


    for dirpath, dirnames, files in os.walk(dirname):
        print(dirpath)

        for file in files:
            print("  L   ", file)

        for d  in dirnames:
            printdirandfile(d)
        

print("-------------------------")
printdirandfile("mydir")
