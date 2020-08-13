
s = "Hello world"
a = [100, 200, 300]
_pi = 3.14

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass

print("module1 : ", __name__)

if __name__ == "__main__":
    print("Initializing module1 ...")
    print(a)
    print(s)
    print(_pi)
    foo('test')
    x = Foo()
    print(x)
    print('Done.')
     