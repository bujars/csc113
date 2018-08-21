x = 7
print(type(x)) #type function tells what type the variable is
x=7.0
print(type(x))
x="bujar"
print(type(x))
x=True
print(type(x))
x=None
print(type(x)) #Nonetype

x="bujar".capitalize()
print(x)
x='seven'.upper()
print(x)
x="SEVEN".lower()
print(x)



#NOTE the f tells the program to not write x inside the brackets, but rather to print the variable that is attached with it. 


x ='seven {} {}'.format(8,9)
print(f'x is {x}')


a=8
b=9
x=f'seven {a} {b}'
print(x)

x=f'seven{a:<05} {b}' #05 means 4 zeros and 1 space to add to the last type
print(x)


#Numerical Type:
x=7/3
print(f'x is {x}') #NOTE its a float not an int

""" #To get a doublr
double(x)=(7/3) #NOTE doesn't work -- will be solved next session. 
print(f'x is {x}')
 """

#NOTE to make int, must change the type
x=int(7/3)
print(f'x is {x}')

#NOTE this is how you get remainder
x = 7%3
print(f'x is {x}')
print(type(x))

x=.1*.1*.1


from decimal import*
a=Decimal('.1') #NOTE a string type must be passed, not a float/double
print(type(a))
b=Decimal('.2')
x=a*a*a-b
print(x)


#bool type

x=True
print(f'x is {x}')
print(type(x))

x=False
print(f'x is {x}')
print(type(x))

x=7>5
print(f'x is {x}')
print(type(x))

x=7<5
print(f'x is {x}')
print(type(x))

x=7==5
print(f'x is {x}')
print(type(x))

x=0
print(f'x is {x}')
print(type(x))

#NOTE x = 0 is False by default
if x:
    print(True)
else:
    print(False)

#NOTE x=/ 0 is True by defult
x = 5
if x:
    print(True)
else:
    print(False)

#NOTE x=None is False by default
x=None
if x:
    print(True)
else:
    print(False)



#NOTE i holds the value or the element, it is not necessarily the index. 
#Also, this type of for loop only works linearly.
x = [1, 2, 3, 4, 5 ]
for i in x:
    print(f'i is {i}')
print()#Prints new line
#NOTE lists are immutable
x[2]=42
for i in x:
    print(f'i is {i}')
print()
#NOTE to add elmenet, adds to the end
x.append(60)
for i in x:
    print(f'i is {i}')


print()
x.remove(2) #NOTE To get ride of an element from the list (Remvoves value, not the key)
for i in x:
    print(f'i is {i}')

print('to print size of x, which is', len(x)) #NOTE the , to add space and value


#NOTE this is a tuple -- it is imutable
x=(1,2,3,4,5) #Uses parentheseis instead of square brackets 
#x[2]=42 #NOTE this is an error, because you cannot change the values in it. 
for i in x:
    print('i is {}'.format(i))

#NOTE in a tuple you can have multiple types
x=(1,2,3,4,'five', 6.0, [7, 8])
for i in x:
    print('i is {}'.format(i))
print(type(x[6])) #Prints the type of that element

#NOTE since tuples are immutable, you cannot add or remove from them, but you can concatenate two together
y=(1,2,3)+(4,2)
print(y)



#Creating integer list with a certain tange
x=range(5) #Starts at 0 and goes up to but doesnt include 5
for i in x:
    print('i is {}'.format(i))
x=range(5,10) #Starts at first, ends at last-1
for i in x:
    print('i is {}'.format(i))
x=range(5,50,10)#starts at first add moves in interval of third up to last
for i in x:
    print('i is {}'.format(i))

#range is immutable -- so here's how to make it mutable
x=range(5)
x=list(range(5))
x[2]=42
for i in x:
    print('i is {}'.format(i))
print()





#Dictionary:

#Defining Hashtable
x={'one':1, 'two':2, 'three':3} #NOTE how it has {}
for i in x:
    print('i is {}'.format(i))
print()
#print(x.values('one')) #NOTE not sure how this function works. 
print(x.items()) #Prints all elements inside of the Dictionary
print(type(x.items))
print(x.values()) #Prints the values of the key: 1,2,3
print(x.keys()) #Prints the keys one,two three

print()
for k,v in x.items():
    print('key is {} and value is {}'.format(k,v))


#NOTE TO create a new dictionary -- mutable
D={}
print(type(D))
D['student ID'] = 12 #NOTE this is one way of adding items to the dictionary
print(D.items())
