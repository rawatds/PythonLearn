name = "Dharmender Rawat"
age = 45
class Emp:
    pass
x = Emp()

print('--------------------------')
print(dir())

from  module1 import a, s
print('--------------------------')
print(dir())

print('--------------------------')
import module1
print(dir(module1))

from module1 import *
print(dir())
