""" A recap of last lesson """


x = [7,8,3,4,5]
#A list can be composed of different object

#THis for loop doesn't represent the indexes, rather the elements
for i in x:
    print('i is {}'.format(i))


#A list is mutable
x[2]=42
print(x)

x.append(2) #add element with value 2 to the end of he list

i=0
a=4
x.insert(i,a) #will insert element with value "a" at index "i"
print(x)

print('size', len(x)) #length of the list


a=5
x.remove(a) #removes the first element with the value 'a'
print(x)
print('size', len(x))


#Lets remove multiple accurances of a value
a=4
print(type(x.remove(a)))
while(a in x):
    x.remove(a)
print(x)
print('size', len(x))


""" i=1
del[i] #deletes element with index "i"
print(x)
print('size', len(x))
 """
#NOTE the above gives an error


x= [11,12,13,14,15,16]
i=0
print(x.pop(i)) #removes the element with index i and returns it
print(type(x.pop(i)))
print(x)

a,b = 70, 80
x.extend([70, 80]) #add list of elements at end
print(x)
print('size', len(x))


#Common error: note that the avoce methods do not "return" the modifed list
#they just modify the original list

a=4
print(type(x.append(a))) #: <class 'NoneType'>
print(type(x.remove(a))) #: <class 'NoneType'>

a=16
print(x.index(a)) #returns the index of the first element with value "a"

a=4
x.extend([a,a,a,a])
print(x)
print(x.count(a)) #returns the imber of times "a" appears in the list.

print(x)
x.sort(key=None, reverse=False) #Sorts in order 
print(x)
x.sort(key=None, reverse=True) #sorts in decreasing order
print(x)

x.reverse() #reverse the order
print(x)




#NOTE the key needs to be figured out next class. if its set to str.capitalize, To is last. With none, To is first
y=["how", "To", "sort"]
y.sort(key=None, reverse=False) #sorts in increasing order
print(y)



##### Moving on to Tuples #####
#a touple is  a seqience of immutable objects in pythong

x = (1, 2, 3)
print(x)
""" print(x[0], type:, type(x[0])) """

y=(1,2,4)+(1,3)
print(y)
print(type(y))

#""" add elements to end of a touple
#x=(1,2,3,4,5, "four", 3.4, [1,3])
#y=6.7
#print(type((y,)))
# """
# print(x)

tuple1 = (0,1,2,3)
tuple2 = ("python", "geek")
print(tuple1+tuple2)
tuple=('python',)*3
tuple=(1,)*100
print(tuple)

#test slicing 
tuple = (0, 10, 20, 30, 40, 50)
print(tuple[1])
print(tuple[1:]) #elements from index 1 to the end
print(tuple[2:4]) #elements from ipythndex 2 to before 4
print(tuple[:])#all the elements
print(tuple[::1]) #slice step is 1 ...basically increments i by 1 and print everything
print(tuple[::2]) #slice step is 2 ...skips one element
print(tuple[::-1]) #slice step is 1 and travels reversely ..goes backaways and prints all
print(tuple[::-2]) #slice step is 2 and travels reversely .. goes backwats and skips by 1 



#Converting tuple to list
x=(10,20,30)
print(list(x)) #NOTE this does not reassign x as a list, just prints it as a list
print(type(list(x)))








### NEXT lets talk about sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) #Shows that duplicates are removed
'orange' in basket
'crabgrass' in basket
a=set('abc')
print(a) #uniqie ;etters in a
b = set('alacazam')
print(b)

#Professor had these commented out -- rechech why
#s="A. B, C, D"
#print(s.split(',')) #prints ['A', 'B']

a - b      #leeters in a but not in b
a | b      #letters in a or in b or both
a & b      #letters in both a and b
a ^ b      #letters in a or b but not both