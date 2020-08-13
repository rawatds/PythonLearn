import sys

def linux_os():
    print("Welcome to os checker...")
    assert ('linux' in sys.platform), "This program only runs in Linux"
    print("Above assertion passed")
   
try:
    linux_os()
except:
    print("Some error was found, but bypassed using try..except")

print("Done")