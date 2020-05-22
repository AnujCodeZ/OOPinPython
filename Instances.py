''' Instance of the class is called object.
This is unique and has all the functionality of the class.'''

class Employee:

    ''' self.
    It is the instance that is passed when the function is called.'''

    # Constructor.
    def __init__(self, first, last, pay):

        # Attributes.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    # Method.
    def fullname(self):

        return f"{self.first} {self.last}"

''' We don't have to pass instance, 
as self is automatically understands it.'''

emp_1 = Employee('Anuj', 'Rana', 50000)
emp_2 = Employee('Test', 'User', 40000)

print(emp_1.email, emp_2.email)

# Methods are called with paranthesis.
print(emp_1.fullname(), emp_2.fullname())

''' We can also use method like this.
Now you can understand what self is.'''

print(Employee.fullname(emp_1))
