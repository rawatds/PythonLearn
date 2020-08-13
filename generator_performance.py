import time, random, memory_profiler as mp

names = ['Dharmender', 'Savi', 'Gurupreet', 'Anil']
progs = ['Java', 'C++', 'Python', '.net', 'NodeJS', 'Cobol']

print("Memory (before): {} Mb".format(mp.memory_usage()))

def people_list(nums):
    result = []
    for i in range(nums):
        person = {
            'id' : i,
            'name' : random.choice(names),
            'prog' : random.choice(progs)
        }
        result.append(person)
    return result


def people_generator(nums):
    for i in range(nums):
        person = {
            'id': i,
            'name': random.choice(names),
            'prog': random.choice(progs)
        }
        yield person


t1 = time.time()
# List
#people = people_list(1000000)

#Generator
for p in  people_generator(1000000):
    pass
t2 = time.time()

print("Memory (after): {} Mb".format(mp.memory_usage()))
print("Total time taken: ", (t2-t1), " seconds")