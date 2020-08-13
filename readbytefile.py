with open('sample.png', 'rb') as reader:
    print(reader.read(1))
    print(reader.read(3))
    print(reader.read(2))
    print(reader.read(1))
    print(reader.read(1))

    