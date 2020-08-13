print(dir())

import pkg.mod1, pkg.mod2

print(dir())
print(pkg)

pkg.mod1.foo()
print(pkg.mod1.Foo())

pkg.mod2.bar()
print(pkg.mod2.Bar())

