#tuple------------------------------------

#a tuple is a sequence of immutable Python objects.

x = (1, 2, 3, 4, 5, "four", 3.4, [1,3])

# x[0]=7 will give an error

for i in x:
    print('i is {}'.format(i))
print(x[6], 'type:', type(x[6]))

y=(1,2,4)+(2,3) #concatenation 
print(y)
print(type(y))

#add elements to end of a tuple:
x=(1, 2, 3, 4, 5, "four", 3.4, [1,3])
y=6.7
print(type((y,)))

x=x+ (y,)
print(x)

y=[1,2,3]
print(type((y,)))
x=x+(y,)

print(x)

print(len(x)) #size of tuple

#merge two tuples
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
print(tuple1 + tuple2)

# create a tuple with repetition 
tuple = ('python',)*3
tuple=(1,)*100
print(tuple)

#test slicing
tuple = (0 ,10, 20, 30,40,50)
print(tuple[1])
print(tuple[1:]) #elements from index 1 to the end
print(tuple[2:4])  #lements from index 2 before index 4
print(tuple[::]) #all the elements
#print(tuple[::0]) error
print(tuple[::1])  #slice step is 1
print(tuple[::2]) #slice step is 2
print(tuple[::-1]) #slice step 1 and traverse reversly
print(tuple[::-2]) #slice step is 2 and traverse reversly 


#converting tuple to list
x = (10, 20, 30)
x=list(x)
print(list(x))
print(type(x))

#max and min of tuple
x = (10, 1100, 30)
print(max(x))
print(min(x))
x = ('ok','elements' , 'random')
print(max(x))
print(min(x))
