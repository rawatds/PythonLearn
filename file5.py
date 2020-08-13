with open('test.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')