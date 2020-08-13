class Employee:

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def __repr__(self):
        return "Employee ({}, {}, {})".format(self.fname, self.lname, self.salary)

    def fullname(self):
        return self.fname + " " + self.lname

    def __str__(self):
        return "Employee {} has salary of Rs {}".format(self.fullname(), self.salary)

    def __add__(self, other):
        # return NotImplemented
        return self.salary + other.salary

emp1 = Employee('Dharmender', 'Rawat', 1000)
emp2 = Employee('Anil', 'Kumar', 2000)

print(emp1)
print(emp2)

print('-------------')
print(repr(emp1))
print(str(emp1))
print(str(emp2))

print('-------------')
print(emp1.__repr__())
print(emp1.__str__())

# print(emp1.__fullname__())  # AttributeError: 'Employee' object has no attribute '__fullname__'
print(emp1.fullname())

print('-------------')
print(emp1 + emp2)
print(emp1.__add__(emp2))
