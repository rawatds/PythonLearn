
# Normal for loop ------------------------------------------------------------

def make_sqr(nums):
    result = []

    for x in nums:
        result.append(x * x)

    return result;

sqrs = make_sqr([1, 2, 3, 4, 5])

print("sqrs: ", sqrs)

# Generator - simple ------------------------------------------------------------
def gen_sqr(nums):
    for n in nums:
        yield n * n;

my_gen = gen_sqr([2, 3,4,5 ,6])
print(my_gen)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
#print(next(my_gen)) # StopIteration

print()

# Iterting a generator
my_gen2 = gen_sqr([10, 20, 30, 40, 50])
for v in my_gen2:
    print(v)

print()

# Generator -- Advanced ------------------------------------------------------------
numns = [11, 22, 33, 44, 55]
adv_gen = (x *x for x in numns)
# OR adv_gen = [x *x for x in numns]
print(adv_gen)
print()

# OR
for v in adv_gen:
    print(v, end='  ')

