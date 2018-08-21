class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self, first, last, pay): #constructor
        self.first = first
        self.last = last
        self.email = first+ '.'+last+'@gmail.com'
        self.pay = pay
        Employee.num_of_emps+=1
    
    def fullname(self): #regular method
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount) #correct -- raise ammount is of instance
        #uses the instance(self raise_amount)
        """ self.pay = int(self.pay*Employee.raise_amount) """ #this uses the employee class raise amount
    
    @classmethod #when you want to use the class method as a constructor
    def from_string(cls, emp_str): #When using class method, you never have to pass self, only class and the other parameters
        first, last, pay = emp_str.split('-') #This splits strings uses dashes
        return cls(first, last, pay) #creates a new instance from first last and pay 
        #--This is given to the constructor to be made 
        #Don't want to directly change constructor, rather find ways to use it. 
    @classmethod
    def set_raise_amt(cls, amount): #note this is a class method because you want to be able to change the variable for the whole class, not just one single attribute
        cls.raise_amount = amount
   
   
    #lets say we dont want to pass instance or class, you must create a static method
    @staticmethod #note how day is an arigement, not cls or self
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    #Special Methods
    def __repr__(self): #unambigious representation of the object --- Note you can call it directyl emp_1.__repr__() or just emp_1
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    #def __str__(self):
    #   return '{} - {}'.format(self.first, self.last)


#Inheritance 

#Lets develop class developer. Note a developer is still a employee

#Note parent class goes in parethesis.
class Developer(Employee): #inherit from Emplyee class
    pass #Note this is needed to pass everything from employee
    raise_amount = 1.1 #changes raise amount for this specific class, not employee class. 
    #Let's say we want to change developer to be even more different. 
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #method 1 ##NOTE simple of of not having to write out everything else, just use the super class one. 
        #Employee.__init__(self,first,last,pay) #method 2
        self.prog_lang = prog_lang

dev_1 = Developer('eli', 'valdhe', 50000, 'java')
print(dev_1.email)
print(dev_1.pay)
print(Developer) #Prints the class
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.prog_lang)

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None): #don't pass mutable datatypes, hence why employees is set to nothing and then changed below. 
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
            print(emp)
        

dev_2 = ('b', 'j', 10000, 'c++')
man_1 = Manager('e', 'v', 50000, [dev_1])
print(man_1.employees) #note you cannot print the employees like this. 
man_1.add_emp(dev_2)
man_1.remove_emp(dev_1)
print(man_1)
man_1.print_emps()


#Things to check about classes. 
isinstance(man_1, Manager)
issubclass(Employee, Manager)

''' --------------------------------------------------------------------------
##Sepcial methods have double underscore in from and at the end
def __init__():
def __repr__(): #unambigious representation of the obkect
    return 'Employee('{}','{}','{}')'
 '''

emp_1 = Employee('eli', 'vahd', 50000)
emp_1
emp_1.__repr__()



##
import cv2 #for reading videos
import os #when we want to work with pths -- ie folders, changing
import numpy as np #not sure
