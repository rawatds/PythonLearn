class Vector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x ** 2 +  self.y ** 2) ** 0.5
    
    def __str__(self):
        return f'{self.x}i{self.y:+}j'

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(3, 4)
v2 = Vector(7, 12)

print(v1)
print(v1.__str__())
print(str(v1))

print(abs(v1))
print(v1.__abs__())

print(repr(v1))
print(v1.__repr__())

print(eval(repr(v1)))
print(type(repr(v1)))

v3 = v1 + v2
print(v1, v2, v3)

