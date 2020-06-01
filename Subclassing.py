''' Inheritance or subclassing.
It allows us to inherit methods and attributes from a parent class.'''

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

class Developer(Employee): # Specify in bracket name of the parent class.
    ''' If we only write pass here.
    It will have all the functionality of Employee.'''
    # Class variable.
    raise_amount = 1.10

    # Constuctor.
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        ''' super method will let subclass use parent classes features in subclass.
        It is equivalent to Employee.__init__(self, first, last, pay)'''
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):

        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):

        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):

        for emp in self.employees:
            print('-->', emp.fullname())  

'''Python follow inheritance chain called method resolution order.
In this Python tracks all the classes that are connected.
You can see this by calling help(class) function.'''
# print(help(Developer))

dev_1 = Developer('Anuj', 'Rana', 50000, 'Python')
dev_2 = Developer('Test', 'User', 40000, 'C++')

print("Accessing parent class features")
print(dev_1.email)

print("Developer class raise_amount.")
''' Here you see dev_1 uses Developer's raise_amount.
Without damaging parent class raise_amount.'''
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print("Accessing Developer's constructor.")
print(dev_1.prog_lang)

print("Creating Manager.")
mgr_1 = Manager('Test', 'Manager', 90000, [dev_1])
print(mgr_1.email)
mgr_1.print_emps()

print("Adding employee.")
mgr_1.add_emp(dev_2)
mgr_1.print_emps()

print("Removing employee.")
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print("Checking instance.")
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print("Checking subclass.")
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))