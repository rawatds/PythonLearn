# Comprehension examples

import timeit
import random
import datetime


# LIST -------------------------------------------------------
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mylist = [n * n for n in nums if n % 2 == 0]
print(mylist)

mylist2 = [(letter, num) for letter in 'abcd' for num in '0123']
print(mylist2)

# DICT -----------------------------------------------------
fname = ['Dharmender', 'Anil', 'Savi', 'Gururpreet']
lname = ['Rawat', 'Kumar', 'Gupta', 'Gururpreet']
fullnames = zip(fname, lname)
print(list(fullnames))
# for n in fullnames:
#    print(n)

my_dict = {}
for fn, ln in zip(fname, lname):
    my_dict[fn] = ln

print(my_dict)

my_dict2 = {fn: ln for fn, ln in zip(fname, lname)}
print(my_dict2)

my_dict3 = {fn: ln for fn, ln in zip(fname, lname) if fn != 'Savi'}
print(my_dict3)

# SET ----------------------------------------------------------
nums = [1, 3, 2, 1, 3, 4, 2, 4, 4, 1, 5]
my_set = set()
for n in nums:     my_set.add(n)
print(my_set)

my_set2 = {n for n in nums if n > 3}
print(my_set2)

# GENERATOR --------------------
nums = [1, 2, 3, 4, 5]
my_gen = (n*n for n in nums if n > 3)
print(my_gen)
for i in my_gen: print(i, end=' ')
print(); print()

mlist = [i for i in range(7)]
print("mlist: ", mlist)
mlist = [0 for i in range(7)]
print("mlist: ", mlist)
mlist = [0 for _ in range(7)]
print("mlist: ", mlist)

matrix = [[i for i in range(5)] for _ in range(6)]
print(matrix)

# WALRUS Operator example ---------------------

def get_temp():
    rnd_temp = random.randrange(90, 110)
    print("Temp generated :", rnd_temp)
    return rnd_temp

hot_temps = [temp for _ in range(10) if (temp := get_temp()) >= 100]
print()
print("Hot temps: ", hot_temps)

print ('----------------------------------------')


start = (datetime.datetime.now())
#print("sum of squr:", sum([i*i for i in range(1000000000)]))    # Will not work, system crashes : MemoryError
print(sum(i*i for i in range(1000000000)))
end = (datetime.datetime.now())
print("Time taken: ", (end - start))


