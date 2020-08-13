with open("sample.txt") as reader:
    print(reader.read())

print('------------------------------------')

with open('sample.txt') as reader:
    print(reader.readline(5))
    print(reader.readline(5))
    print(reader.readline(5))
    print(reader.readline(5))

print('------------------------------------')

f = open('sample.txt')
#print(f.readlines())   

print(list(f))