try:
    with open('pkg/mod1.py') as reader:
        line = reader.readline()

        while line != '' :       # while not EOF
            print(line, end='')
            line = reader.readline()
except Exception as error:
    print(error)

print()
print("Done! -------------------------")

with open("sample.txt") as reader:
    for line in reader.readlines():
        print(line, end='')

print()
print("Done! -------------------------")

