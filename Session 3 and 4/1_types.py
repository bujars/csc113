#!/usr/bin/env python3

#Overview----------------

x = 7
print(type(x))

x=7.0
print(type(x))

x='7'
print(type(x))

x=True
print(type(x))

x=None
print(type(x))

#String type-----------------------

x='seven'  #no difference between ' ' and " "
x="seven"
 
x='seven'.capitalize()
print(f'x is {x}')
x='seven'.upper()
print(f'x is {x}')
x='SEVEN'.lower()
print(f'x is {x}')

x='seven {} {}'.format(8,9)
print(f'x is {x}')
x='seven {1} {0}'.format(8,9)
print(f'x is {x}')

a=8
b=9
x=f'seven {a} {b}'
print(x)

a=8
b=9
x=f'seven {a:<5} {b}' #adding space
print(x) 


a=8
b=9
x=f'seven {a:<05} {b}' #adding zeros and space
print(x) 

#Numeric type -------------------------------------

x=7 / 3
print(f'x is {x}')
print(type(x))

x=7 // 3  # int result, alternatively: int(7/3)
print(f'x is {x}')
print(type(x))

x=7 % 3
print(f'x is {x}')
print('x is {}'.format(x))
print(type(x))

x=.1+.1+.1-.3
print(f'x is {x}')
print(type(x))  #floar: too high precision 

from decimal import * 
a=Decimal('.1')
print(type(a))
b=Decimal('.3')
x=a+a+a-b
print(f'x is {x}')
print('x is {}'.format(x))
print(type(x))

from decimal import * 
a=Decimal(.1)
b=Decimal(.3)
x=a+a+a-b
print(f'x is {x}')
print(type(x))

#bool type ------------------------------

x = True
print(f'x is {x}')
print(type(x))

x =False
print(f'x is {x}')
print(type(x))

x = 7 > 5
print(f'x is {x}')
print(type(x))

x = 7 < 5
print(f'x is {x}')
print(type(x))

x = 7 == 5
print(f'x is {x}')
print(type(x))

x =0 #statement: set to zero: by default false  
print(f'x is {x}')
print(type(x))
if x:
    print("True")
else:
    print("False") 

x =5 #statement: any non zero number: by default true 
print(f'x is {x}')
print(type(x))
if x:
    print("True")
else:
    print("False") 

x ="" #statement: empty string: by default false
print(f'x is {x}')
print(type(x))
if x:
    print("True")
else:
    print("False") 

x ="ok" #any non empty string: by default true
print(f'x is {x}')
print(type(x))
if x:
    print("True")
else:
    print("False") 

x =None #statement: none string: by default false
print(f'x is {x}')
print(type(x))
if x:
    print("True")
else:
    print("False") 

