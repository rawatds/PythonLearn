class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        #self.email = ''

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    # @email.setter
    # def email(self, newemail):
    #     self.email = newemail         # RecursionError: maximum recursion depth exceeded

    def __str__(self):
        return '{} {} has email {} and fullname: {}'.format(self.first, self.last, self.email, self.fullname)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, fullname):
        first, last = fullname.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Deleting fullname property")
        self.first = None
        self.last = None

emp1 = Employee('Dharmender', 'Rawat')
print(emp1)

emp1.first = "Anil"
print(emp1)
print(emp1.fullname, emp1.first, emp1.last)

# print(emp1.first, emp1.last)

#emp1.email = 'abc.xyz@gmail.com'
#print(emp1)

print(dir(emp1))

print('-----------------------')
del emp1.fullname
print(emp1)
print(emp1.fullname, emp1.first, emp1.last)
print(dir(emp1))


