''' Magic methods:
These are special methods of the class to get some more functionality.
These methods are surrounded by double underscore generally called Dunder.'''

class Employee:

    # Class variables.
    no_of_emps = 0
    raise_amount = 1.04

    # Constructor.
    def __init__(self, first, last, pay):

        # Attributes.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.no_of_emps += 1 
    
    # Method.
    def fullname(self):

        return f"{self.first} {self.last}"

    def apply_raise(self):

        self.pay = int(self.pay * self.raise_amount)

    # Magic methods.
    # Representation methods.
    def __repr__(self):

        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"
    
    def __str__(self):

        return f"{self.fullname()} -- {self.email}"

    # Overload methods.
    def __add__(self, other):

        return self.pay + other.pay


emp1 = Employee('Anuj', 'Rana', 50000)
emp2 = Employee('Test', 'User', 40000)

print("Magic Methods.")
print(emp1)

# For specific.
print("Explicitly calling.")
print(repr(emp1))
print(str(emp1))

# Overloading add method.
print("Overloading add method.")
print(emp1 + emp2)