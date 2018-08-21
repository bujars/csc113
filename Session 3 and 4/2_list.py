#!/usr/bin/env python3

#list-------------------------
 
x = [ 7, 8, 3, 4, 5 ]
for i in x:
    print('i is {}'.format(i))

x=[7, "four", [3,4,5]]  #a list of different objects
for i in x:
    print('i is {}'.format(i))

#list is mutable:
x = [ 1, 2, 3, 4, 5 ]
x[2]=42
print(x)

a=60
x.append(a) #add element with value "a" to the end of the list
print(x)

i=0
a=4
x.insert(i, a) #will insert element with value "a" at index "i"
print(x)

print('size', len(x)) #length of the list 

a=5
x.remove(a) #remove the first element with value "a"
print(x)
print('size', len(x))


x=[1,1,4,5,6,1]
a=1
print(type(x.remove(a)))
while(a in x):
    x.remove(a)

print(x)

a=4
x.remove(a) #only the first "a=4" is removed 
print(x)
print('size', len(x))

i=1
del x[i]  #delete element with index "i" 
print(x)
print('size', len(x))

x=[11,12,13,14,15,16]
i=0
print(x.pop(i))  #removes the element with index i and returns it 
print(type(x.pop(i)))
print(x)

a, b =70, 80
x.extend([a, b])  ## add list of elements at end 
print(x)

#Common error: note that the above methods do not *return* the modified list
# they just modify the original list.
print(type(x.append(13)))

a=4
print(type(x.append(a))) #: <class 'NoneType'>
print(type(x.remove(a))) #: <class 'NoneType'>

a=60
print(x.index(a)) #returns the index of the first element with value "a"

a=4
x.extend([a,a,a,a])
print(x)
print(x.count(a))  #returns the number of times "a" appears in the list.

print(x)
x.sort(key=None, reverse=False) #sorts in increasing order
print(x)
x.sort(key=None, reverse=True) #sorts in decreasing order
print(x)

x.reverse() #reverse the order 
print(x) 

y=["how", "To", "sort"]
y.sort(key=str.capitalize, reverse=False) #sorts in increasing order
print(y)