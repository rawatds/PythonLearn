print(dir())

from pkg.mod1 import foo
print(dir())

foo()
#Foo()   # NameError: name 'Foo' is not defined

from pkg.mod2 import Bar as BB
print(dir())

print(BB())

from pkg import mod1
print(dir())

mod1.foo()
print(mod1.Foo())
