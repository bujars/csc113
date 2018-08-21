#Recap of last lesson
#---------------------------------------------------------------------------#
#to go through a file, the most efficent way is to convert it into a list -
# -which would then allow you to access each line via indice

#f.read() --outputs each line in one sing line. 

#4 diffenet file modes -- read, write, appeand, read and write

#f.readfiles() -- is a method to convert lines into a list. 

#line.startwith('STRING') --Checks to see if a certain line starts with that word. 

#You can seek inside of files, 
# it goes to the nth position in the file f.seek(n) and sends you to the end of that position, 
# meaning if you read the next line, it reads the n+1 word/leeter
#Has two arguments, seek.(offset,from_what) ##from_what has three values, 0, 1, 2 
#0 = start from current position (ie, nth position)
#1 = also current position but in binary format
#2 = start from end of file (must open file from rb+ form --read and write in binary format) 
# THus ^ must seek negative values to go backwards, otherwise it will bring a empty string 
# (NOTE in printing you will always see character b -- ignore, just tells you your in binary mode.)


#NEW MATERIAL
#Changing name of file/opening new directory 
import os
os.rename("workfile.txt", 'workfile3.txt')
f = open('workfile4.txt', 'w')
f.close()
os.remove('workfile4.txt')
os.mkdir("test")
os.getcwd()
#newpath = #Enter path here
#os.chdir(newpath) #set current path to the new path


#Classes

#NOTE an empty class is infact useless, becuase you're going to indivualy give it their information. 
""" class Employee:
    pass #Nothing inside of class, but it doesnt return an error -- empty class

#2 different instances of employees 
emp_1 = Employee()
emp_2 = Employee()
print(emp_1)
print(emp_2)
#notice how these two are different ^^ """

""" class Employee:
    #self means its from this class --> think of this from c++ or java
    def __init__(self, first, last, pay): #constructor
        self.first = first
        self.last = last
        self.email = first+ '.'+last+'@gmail.com'
        self.pay = pay
    
    def fullname(self): #regular method
        return '{} {}'.format(self.first, self.last)

    #class variable vs instance variables
    def apply_raise(self):
        #self.pay = int(self.pay*1.04) #returns error 
        

emp_1 = Employee('eli', 'vahd', 50000)
emp_2 = Employee('test', 'user', 60000)

print(emp_1.fullname()) #call method on instance 
print(emp_2.fullname())
print(Employee.fullname(emp_1)) #note this way also works

print(emp_1.email) #lets you print certain variables that it holds
print(emp_2.email)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

 """

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
        self.pay = int(self.pay*Employee.raise_amount) #this uses the employee class raise amount
    
    @classmethod #when you want to use the class method as a constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-') #This splits strings uses dashes
        return cls(first, last, pay) #creates a new instance from first last and pay 
        #--This is given to the constructor to be made 
        #Don't want to directly change constructor, rather find ways to use it. 

    

emp_1 = Employee('eli', 'vahd', 50000)
emp_2 = Employee('test', 'user', 60000)

print(emp_1.fullname()) #call method on instance 
print(emp_2.fullname())
print(Employee.fullname(emp_1)) #note this way also works

print(emp_1.email) #lets you print certain variables that it holds
print(emp_2.email)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.num_of_emps)
emp_1.num_of_emps #insance variable is useless

emp_1.pay
emp_1.apply_raise()
emp_1.pay

emp_1.raise_amount = 1.06
emp_1.pay = 50000
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