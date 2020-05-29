''' Class methods:
A regular method automatically takes instance as first argument.
If we want to take automatically class as first argument class methods will work.
Static methods:
They don't recieve anything like class or instance as first arguments.
They are just functions which have logical connections with class.'''

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
    
    # Methods.
    def fullname(self):

        return f"{self.first} {self.last}"

    def apply_raise(self):

        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod # This decorator makes class methods.
    def set_raise_amount(cls,  amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):

        first, last, pay = emp_str.split('-')

        return cls(first, last, pay)
    
    @staticmethod # This decorator maked static class.
    def is_workday(day): # Here this function didn't take any class or instance.
        # In datetime module weekday() returns number like for Monday, its 0.
        if day.weekday() == 5 or day.weekday() == 6: # Taking off in Saturday and Sunday.
            return False
        return True


emp1 = Employee('Anuj', 'Rana', 50000)
emp2 = Employee('Test', 'User', 40000)

''' Class methods are call by class.
calling by instance makes no sense.'''

print("Class method Using by class:")
Employee.set_raise_amount(1.05)
print(Employee.raise_amount)
print(emp1.raise_amount)

''' Class methods can be used as alternative constructor.
Suppose we want to create employee from string input.'''

emp_str_1 = "Anuj-Rana-60000"
emp_str_2 = "Test-User-50000"

''' What we do.
We create a class method for that and set values to attributes.'''

print("From string method:")

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)

print(new_emp_1.email)
print(new_emp_2.email)

# Importing datetime.
import datetime

my_date = datetime.date(2020, 5, 30) # This day its Saturday.

print("Using static method:")
print(Employee.is_workday(my_date))