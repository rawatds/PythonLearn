print("mod1 ...")

__all__ = ['foo']

def foo():
    print("[mod1].foo()")

class Foo:
    pass


def zoo():
    from pkg import pkg_A
    print("Inside mod1.zoo, pkg_A = ", pkg_A)
