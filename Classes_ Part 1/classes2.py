#class variables vs instance variables
'''
class Employee:

    def __init__(self, first, last, pay):  #constructor 
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay=int(self.pay * 1.04)

emp_1 = Employee('eli', 'vahd', 50000)
emp_2 = Employee('test', 'user', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
'''
#-----------------------------------------------------------------------------------
'''
class Employee:
    raise_amount=1.04

    def __init__(self, first, last, pay):  #constructor 
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        #self.pay=int(self.pay * raise_amount) returns error
        self.pay=int(self.pay * self.raise_amount)  #correct: raise_amount of instance
        #self.pay=int(self.pay * Employee.raise_amount)  #correct: raise_amount of class

emp_1 = Employee('eli', 'vahd', 50000)
emp_2 = Employee('test', 'user', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount) #the class has this attribute 
print(emp_2.raise_amount)

print(emp_1.__dict__) # there is no "raise_amount" (not the instance variable)
print(Employee.__dict__) #we can see the raise_amount


Employee.raise_amount=1.05
print(Employee.raise_amount)
print(emp_1.raise_amount) 
print(emp_2.raise_amount)

#creating the instance variable 
emp_1.raise_amount=1.06 #can not change the value for the class
print(Employee.raise_amount)
print(emp_1.raise_amount) 
print(emp_2.raise_amount) #has not been changed 


Employee.raise_amount=1.07 
print(Employee.raise_amount) 
print(emp_1.raise_amount) #important: still equal to 1.06!
print(emp_2.raise_amount)

print(emp_1.__dict__) # raise_amount variable is added to the dictionary 

emp_3=Employee('bob','w',5000)
print(emp_3.raise_amount)
print(emp_3.__dict__) 
'''
#-------------------------------------------------------------------------------------
'''
class Employee:
    raise_amount=1.04
    num_of_emps=0 
    def __init__(self, first, last, pay):  #constructor 
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_emps+=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        #self.pay=int(self.pay * raise_amount) returns error
        self.pay=int(self.pay * self.raise_amount)  #correct: raise_amount of instance
        #self.pay=int(self.pay * Employee.raise_amount)  #correct: raise_amount of class

emp_1 = Employee('eli', 'vahd', 50000)
emp_2 = Employee('test', 'user', 60000)
print(Employee.num_of_emps)

emp_3 = Employee('E1', 'user', 60000)
print(Employee.num_of_emps)

emp_2.num_of_emps #instance variable is useless in this example 
'''
#---------------------------------------------------------------------------------------
'''
class Employee:
    raise_amount=1.04
    def __init__(self, first, last, pay):  #constructor 
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)  #correct: raise_amount of instance
        #self.pay=int(self.pay * Employee.raise_amount)  #correct: raise_amount of class

emp_1 = Employee('eli', 'vahd', 50000)
emp_1.pay
emp_1.apply_raise()
emp_1.pay #4 percent

emp_1.raise_amount=1.06
emp_1.pay=50000
emp_1.apply_raise()
emp_1.pay #equal to 4 percent if we use class variable inside apply_raise and equal to 6 percent if we use instance varibale inside apply_raise
'''