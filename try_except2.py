import sys

def linux_os():
    print("Welcome to os checker...")
    assert ('linux' in sys.platform), "This program only runs in Linux"
    print("Above assertion passed")
try:
    linux_os()
    with open("unknown.file") as file:
        read_data = file.read()
except FileNotFoundError as fnfe:
    print(fnfe)
except AssertionError as error:
    print(error)


print("Done")