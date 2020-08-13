import sys
print(sys.platform)

assert ('linux' in sys.platform), "This program only runs in linux"
print("Hello world")