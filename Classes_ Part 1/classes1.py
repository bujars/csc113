'''
class Employee:
    pass   

emp_1 = Employee()
emp_2 = Employee()

#data is unique to each instance:
print(emp_1) 
print(emp_2)

emp_1.first='eli'
emp_1.last='vahd'
emp_1.email='eli.vahd@company.com'
emp_1.pay=50000

emp_2.first='test'
emp_2.last='user'
emp_2.email='test.user@company.com'
emp_2.pay=60000

print(emp_1.email) 
print(emp_2.email)
'''

#-------------------------------------------------------------------------------------
'''
class Employee:

    def __init__(self, first, last, pay):  #constructor s
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

emp_1 = Employee('eli','vahd',50000)
emp_2 = Employee('test','user',60000)

print(emp_1.email) 
print(emp_2.email)
'''
#------------------------------------------------------------------------------------
'''
class Employee:

    def __init__(self, first, last, pay):  #constructor s
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('eli', 'vahd', 50000) #a random number is chosen here! :-)
emp_2 = Employee('test', 'user', 60000)
 
print(emp_1.fullname()) #call method on instance
print(emp_2.fullname()) 
#print(emp_2.fullname) #error 
print(Employee.fullname(emp_1))  #call the method from class and pass the instance

emp_1.__dict__
Employee.__dict__
'''