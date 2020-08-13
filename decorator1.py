print ("============ Function as a Decorator =====================")
def decorator_func(orig_func):
    def wrapper_func(*args, **kwargs):
        print("I'm wrapper_func")
        return orig_func(*args, **kwargs)

    return wrapper_func

@decorator_func
def display():
    print("I'm display function")

@decorator_func
def display_info(name, age):
    print("display_info ran with args ({}, {})".format(name, age))


display()
display_info('Dharm', 45)

print('----------------------')
#display = decorator_func(display)      # Legal, but now no need after @decorator_func
display()

print ("\n============ Class as a Decorator =====================")

class decorator_class(object):

    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print("Before calling {}".format(self.original_func.__name__))
        return self.original_func(*args, **kwargs)

@decorator_class
def printme():
    print("This is printme()")

@decorator_class
def summe(a, b):
    print("Sum of {} and {} is {}".format(a, b, a+b))

printme()
summe(5, 9)

