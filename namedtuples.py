from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

col = Color(50, 100, 150)

print(col[0])
print(col.green)

mycol = Color(red=100, blue=200, green=300)
print(mycol.blue)
print(mycol)

