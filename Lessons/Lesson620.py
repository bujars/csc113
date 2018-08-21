basket = {'apple', 'orange', 'apple', 'pear'} #THIS is how you defind a set
print(basket)
print()

""" #fast memeber testung:
'orange' in basket
'banana' in basket """

primes = {2, 3, 5, 7, 11, 2, 2, 2}
for num in primes:
    print(num)

A={1,2,3}
print(1 in A, 4 not in A)

#operations on sets
A=set('apple')
B=set('orange')

""" A-B
A|B
A&B
A^B  """

s1 = {'a','b','c'}
s2={'b','c','d'}
s3 = s1.union(s2) #gets the union and stores it
print(s3)
s1.update (s2) #updates s1 to the union of s1 and s2
print(s1)
s1.add('1') #adds element to a set
print(s1)
s3=s1.intersection(s2) #intersection of two sets
print(s3)
s1.difference_update(s2) #removes all elements of set2 from set1
print(s1)

s1 = {'a','b','c'}
s2={'c', 'd', 'e'}
s1.intersection_update(s2) #updates s1 with the intersection of itself and s2
print(s1)
print(s2)

s1 = {'a', 'b', 'c'}
s2 = {'c', 'b'}

#Certain functions that u can print
print(s1.isdisjoint(s2))
print(s2.issubset(s1))
print(s1.issuperset(s2))

#symetric difference  means all
s1= {'a', 'b', 'c'}
s2 = {'b', 'c', 'd'}

s3 = s1.symmetric_difference(s2) #removes all the intersected elements and unionizes them
print(s3) #prints a d

s1.discard('a') # removes a from the 
s1.discard('d') #does nothing since d doesnt belong to the set
print(type(s1.discard('e')))
print(s1)
s1.remove('b') #removes b from the set
print(s1)
print(type(s1.remove('c')))
#s1.remove('e') #returns error because 'e' is not in the set
print()
s1 = {'a', 'b', 'c'}
print(s1)
print(s1)
s1.pop() #removes first element? -- NOt sure


print(s1) 

s1='apple'
s2 = 'orange'


s = {x for x in s1 if x not in s2}
print(s)

set1=set() #defines an empty set
for x in s1:
    if x not in s2:
        set1.add(x)
print(set1) #prints the intersection

set1 = set()
for x in s1:
    set1.add(x)
for x in s2:
    set1.add(x)
print(set1) #prints the union




###DICTIONARIES are the most useful datastrcutre in python

#Dictionaries are mutable
x = {'one':10, 'two':20, 'three':30} #itmes:(one, 10) key: one, value:10
print(x)
for i in x:
    print('i is {}'.format(i)) #prints keys not values

x.keys() # returns keys
x.values() # returns values
x.items() #returns of items

#I think the comments below are incorrect -- about the class stuff
print(type(x.keys())) #class 'builtin_function_or_method'
print(type(x.values())) #class 'dict_keys'
print(type(x.items())) #class 'bulltin_functor_or_method'


for k in x.keys():
    print(k)
print()
#prints only the keys

for v in x.values():
    print(v)
print()
#prints only the values

for k,v in x.items():
    print('key is {} and value is {}'.format(k,v))
print()
#prints the key and value 

K=x.keys() #this is not a list!
print(K)
#print(K[0]) #error. its not a list thus cannot access stuff via index

#convert to list:
values_list = list(x.values())
print(values_list)
print(values_list[0]) #now that its a list, u can access specific indexes 

keys_list = list(x.keys())
print(keys_list)
print(keys_list[0]) 

items_list = list(x.items())
print(items_list)
print(items_list[0]) 
print(type(items_list[0])) #each item inside becomes a tuple

x={'A':30, 'B':20, 'C':40, 'D':10}
print(x)
#this isn't working for me 
sorted(x.values(), reverse = False) #sorts the values of the dictionary in reverse order
print(x)

#sorted based on values of the dictionary, not the keys, even though it says key
s= sorted(x, key=x.get, reverse=True) #key -- keep typing here to see what this function does
D={}
for k in s:
    print(f'k is {k}, value is {x[k]}')
    D[k] = x[k] #add k to D, assign the value of k 
print(D)

del x['A'] #why is this not using the previously sorted set? ---- Because u are deleteing from X, not D. 
print(x)
#items are removed from their key

x['B'] = None #sets a new value to a key
print(x)


d={}
seq = ['height', 'width', 'length']
d=d.fromkeys(seq, 0) #the keys in the dictionary will be the keys from seq all set with the value of 1 -- THis is a good way for initalization
print(d)
print(type(d))

D= {}
print(type(D))
D['student ID']=100
D = {"student ID":100, 'name':'Tom'}
print(D.items())
D['age']=20
print(D.items())
print(D)


#Dictionaries are mutable:
D['age']=18
print(D)

#dictionaries of lists
D={}
D['student ID']=[]
D['name']=[]
D['age']=[] 
print(D)

print(type(D)) #dictionary
print(type(D['student ID'])) #list -- thus we can add items to the list

D['student ID'].append(100)
D['student ID'].append(200)
print(D)

#to access the values now of ^^
l = D['student ID'] #create a list of the list of values at this key
print(l[0]) #access elements as u would


