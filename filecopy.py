

with open('fruits.txt', 'r') as rf:
    with open('fruits2.txt', 'w') as wf:

        for line in rf:
            print("Copying ...", line, end='')
            wf.write(line)

print('-------------------------')

with open('fruits.txt', 'r') as rf,   open('fruits3.txt', 'w') as wf:
    for line in rf:
        wf.write(line)
