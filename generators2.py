def multi_yield():
    yield "one"
    yield "two"
    yield "three"

gc = multi_yield()
print(next(gc))
print(next(gc))
print(next(gc))
#print(next(gc))         # StopIteration

print('-----------------------------------')

filename = "employee.csv"

lines = (line for line in open(filename))
listline = (s.rstrip().split(",") for s in lines)
print(next(listline))
print(next(listline))
print(next(listline))