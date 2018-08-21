#Review

#Basics of a class
 
""" class Employee:
"""
#Empty class, but arbitraary attributes can be made -- though is useless

""" class Employee:
    def __init__(): #The __init__is to define a constructor. Parameters go there if you want to set certain values for it.
"""

#Making instances 
#variable = className(paramters)

#regular methods need the "self" -- must pass instance 
""" 
    def fullname(self):
        return self.name #etc...
"""


""" emp1.__dict__ """ #can print the object as a dictionary. 

#if argumenet is self, it uses instance, and this s regular method
"""     def apply_raise(self):
        self.pay=int(self.pay*1.04)  """
#not good because maybe you dont want 1.04 to be a set value. 
# Can make it as a public variable/attribute

#Class attributes are not present in the dictionaries of each instance, meaning if you make the raise a public variable, a
# nd print dictionary for empl, you wont see the 1.06

#2 Main applications of methods
""" @classmethod //When used as a "constructor"
def set_raise_amt(clas, amount): #for the first argumenet you must pass the cls
    clr.raise_amt = amount
"""



""" ------------------------------------------------------------------------------------------------------------------------- """



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

        




emp_1 = Employee('eli', 'vahd', 50000)
emp_2 = Employee('test', 'user', 60000)


import datetime
my_date = datetime.date(2018, 7, 10)
my_date.weekday() #0 stands for monday
Employee.is_workday(my_date)




Employee.raise_amt(1.05)

emp_1.pay
emp_1.apply_raise()
emp_1.pay




#@classmethod working
#lets say the employee is just a string
emp_str_1 = "John-Doe-70000"
#We dont want to convert it to an employee each time, like 
emp_3 = Employee("John", 'Doe', 70000)
#Therefore we create a new way to make employees

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_1.first
new_emp_1.last
new_emp_1.pay



#importing datetime from python 

import datetime

""" #The first class method 
@classmethod
def fromtimestamp(cls, t):
    "constructs a date from a POSIX timestamp (like time.time())"
    y,m,d,hh,mm 
#etc, all this can be fround from datetime class """

lst = emp_str_1.split('-') #split allows us to convert it into a list
lst

#Note if you want to split a string into varibales into the class, the values much match the number of variables.