def square(x):
    return x * x

f = square(5)
print(square)
print(f)

# Assigning a var to function
g = square
print(g)
print(g(5))

# Passing function as arg
def my_map(func, my_list):
    result = []

    for i in my_list:
        result.append(func(i))

    return result

sqs = my_map(square, [1,2,3,4,5])
print(sqs)

# Returning a function
def multiplier(first):
    def multiply(second):
        return first * second

    return multiply


a = multiplier(5)
print(a)
print(a(3))
