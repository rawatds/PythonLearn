import sys

class Order:

    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __add__(self, other):
        #self.cart.append(other)
        #return self
        # OR
        a = self.cart
        a.append(other)
        return self.__class__(a, self.customer)

    def __radd__(self, other):
        #self.cart.insert(0, other)
        #return self
        # OR
        a = self.cart
        a.insert(0, other)
        return self.__class__(a, self.customer)

    def __getitem__(self, key):
        return self.cart[key]

    def __str__(self):
        return f'{self.customer} has {self.cart} in cart.'

    def __bool__(self):
        return len(self.cart) > 0

    def __len__(self):
        return len(self.cart)


order1 = Order(['apple', 'banana', 'mango'], 'Dharmender')
order2 = Order([], "Anil")

print(order1)
print(order2)

print("###", order1.__class__, order1.__class__.__name__)

print(bool(order1))
print(bool(order2))

for order in [order1, order2]:
    if order:
        print(f"Processing order for {order.customer} ...")
    else:
        print(f"Nothing to process for {order.customer}")

print(len(order1))
print(len(order2))

print(order1[0])
print(order1[-1])   # from right side

# ------ add(), radd() -------
print(order1.cart)

order1 = order1 +  'kiwi'
print(order1.cart)

order1 = 'coconut' + order1
print(order1.cart)

print("=================================")
print(sys.path)
print(sys)
#print(sys.__file__) # AttributeError: module 'sys' has no attribute '__file__'

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

import getter_setter
print(getter_setter.__file__)
print(getter_setter)

import re
print(re.__file__)

