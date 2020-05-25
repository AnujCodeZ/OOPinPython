''' Class variables.
These are class dependent not instance dependent.
These can access by class as well as by the instances.'''

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
        ''' Here it has to be Employee.no_of_emps.
        Because, no_of_emps is not instance specific.'''
    
    # Method.
    def fullname(self):

        return f"{self.first} {self.last}"

    def apply_raise(self):

        self.pay = int(self.pay * self.raise_amount)
        ''' Here it has to be self.raise_amount.
        Because, raise_amount may be instance specific.'''


emp1 = Employee('Anuj', 'Rana', 50000)
emp2 = Employee('Test', 'User', 40000)

# Class variable can be accesed by class itself or by instance.
print("Accessing Class variable.")
print(Employee.raise_amount)
print(emp1.raise_amount)

# It can be changed.
print("Changed by Class")
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp1.raise_amount)

# When changed by instance an variable is created for that instance.
print("Changed by an instance.")
emp1.raise_amount = 1.00
print(emp1.raise_amount)
print(Employee.raise_amount)
print(emp2.raise_amount)

print("Employee count", Employee.no_of_emps)
print("Same if accessed by an instance", emp1.no_of_emps)

# We can check all elements in class or in an instance by this.
print("Class dictionary.")
print(Employee.__dict__)
print("Instance dictionaries.")
# Here you also see that emp1 hase raise_amount but emp2 not.
print(emp1.__dict__)
print(emp2.__dict__)