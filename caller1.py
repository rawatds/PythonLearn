import module1

#print(a)           # NameError: name 'a' is not defined
print(module1.__file__)
print(module1.a)
print(module1.s)
print(module1._pi)
module1.foo('hi')
#x = Foo()           # NameError: name 'Foo' is not defined
x = module1.Foo()
print(x)

print('-----------------')


a = ['apple', 'banana']
print(a)

#print(s)    # NameError: name 's' is not defined

from module1 import a, foo
print(a)
foo([1,2])

print('-----------------')

from module1 import *
print(a)
print(s)
print(Foo)
#print(_pi)          # 


print('-----------------')

a = ['apple', 'banana']
from module1 import a as ar, s as st
print(a)
print(ar)
print(st)

print('-----------------')
# Testing unsuccessful imports

try:
    import unknown_module
except ImportError:
    print("The module 'unknown_module' not found")
print('-----------------')

try:
    from mod import unknown_obj
except ImportError:
    print("The object 'unknown_obj' not found")
print('-----------------')
