
try:
    f = open("abc.txt")

    print("Hello")    

finally:
    f.close()
    print("File closed.")
