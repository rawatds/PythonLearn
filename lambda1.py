from functools import  reduce

sq = lambda a: a * a
print(sq(5))

sum3 = lambda a, b, c: a + b + c
print(sum3(10, 20, 14))

print('--------------------------------')

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_even(n):
    return n % 2 == 0

evens  = list(filter(is_even, nums))
print(evens)

odds = list(filter(lambda n : n % 2!= 0, nums))
print(odds)


sqs = list(map(lambda x: x*x, nums))
print(sqs)

sum  = reduce(lambda a, b: a+b, nums)
print("sum", sum)

print("------- sorting name based on lname ------------")
users = ['Dharmender S Rawat', 'Anil Kumar', 'Savi Gupta', 'Gurupreet', 'Rita Devi']
print(users)

users.sort(key= lambda  name: name.split(" ")[-1].lower())
print(users)




