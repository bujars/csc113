#Chapter 4 is all about for loops and stuff

magicians = ['alice', 'david', 'carolina'] #defined the list
for magician in magicians: #defined a for loop / for each. Tells Python to pull a name from the list and store it into magicians
    print(magician)
print()
#You can do much more than just print inside of a for loop

magicians = ['abc', 'bc', 'c']
for magician in magicians:
    print(magician.title()+ ', that was a great trick!') #the title fucntion capitilizes the first letter in the string
print()
#NOTE that in these for loops, everything prints on seperate lines. 

#Lets add a second line inside our loop to show that we can add much more

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

#NOTE \n adds a new line just like in c++ java

#Anything after the for loop just prints once,
print('Thanks for the show')
print()

#Making Numerical Lists
#Using the range function --- range()

for value in range(1,5):
    print(value)
print()
#NOTE range(x, y) prints starting from x up to y, does not include y.

for value in range(1,6):
    print(value)
#now we have 1-5
print()

#The range of numbers can be directly converted into a list, using the list() function

numbers=list(range(1,6)) #NUMBERS is now a list of integers that holds the values 1,2,3,4,5
print(numbers) #NOTE this prints the list in list format
print()

#The range function can also be used to skip certain values
even_numbers = list(range(2,11,2)) #Start at 2, end before 11, and +2 to each value
print(even_numbers)
print()

#Lets print the square of the first 10 numbers
#NOTE: ** means exponent in python
squares = [] #Make an empty list of squares
for value in range(1,11):   
    square = value**2 #create a temporary int variable to hold the sqaure
    squares.append(square) #add the value to the end of the list
print(squares)
print()

#NOTE you can remove the temportary variable
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
print()

#You can easily find out the min, max, and sum of a list of numbers --
#  works for integers and decimals ... as seen below
digits = [1, 2, 3, 4, 5, 6]
digs = [1, 5, 2, 4, 3, 6]
dec = [1.0, 3.4, 2.3, 1.7]

print(min(digits))
print(max(digits))
print(sum(digits))

print()
print(min(digs))
print(max(digs))
print(sum(digs))
print()

print(min(dec))
print(max(dec))
print(sum(dec))
print()


#NOTE, lists can be writen on one line, following list comprehension.
# A list comprehension combines the for loop and the creation of new elements i
# nto one line and eppends them as new elements

squares = [value**2 for value in range(1,11)]
print(squares)
print()

#The syntax is as follows:
#   Begin with a descriptive name for the list
#   Next, use the list brackets to have the defined value -- include the defined expression
#   ie, value**2... THEN write the for looop to generate the values you want to feed into the loop









##NEXT, Working with slicing -- part of a list.
#You specify the first and last index that you want. [x, y) in this range

players = ['c', 'd', 'e', 'f', 'g']
print(players[0:3]) #c, d, e
print(players[1:4]) #d e f
print(players[:4]) #c d e f -- NOTE, if the beginning index is omitted, it starts from the beginning of the list
print(players[2:])#e f g -- NOTE, if the end index is ommitted, it ends at the end of the list


print(players[-3:]) #e f g? --NOTE, a negative index returns an element a certain distance from the end of a list

#NOTE you can loop through a slice
for player in players[:3]:
    print(player.title()) #Prints the first three names, c d e in title format



#NOTE slicing can be utalized for copying lists

my_foods = ["pizza", 'cake', 'fries', 'burger']
friend_foods = my_foods[:] #NOTE by omitting a starting and an ending index, we can get the whole originals list

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
print()

#Lets show how each list is actually different

my_foods.append('bujar')
friend_foods.append('dee')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
print()

#NOTE You cannot copy a list without slicing. 

#Ie this method will make the two variables point at the same list
my_f = ["pizza", "fries"]
dee_f = my_f
my_f.append('cake')
dee_f.append('cheese')

print("My favorite foods are:")
print(my_f)
print("\nMy friend's favorite foods are:")
print(dee_f)
print()

#NOTE how both list are exactly the same. 



#NEXT is Tuples

#Again, Tuples are lists that cannot be changed, ie are immutable 
#Looks like a list but instead of brackets, parenthesis are used. 


#defining a tuple
dimensions = (200, 50)
#To access elements, same as list 
print(dimensions[0])
print(dimensions[1])
print()

""" dimensions[0] = 250 """
#NOTE the above code doesn't work because a tuple is immutable

#Looping in tuples is the same as lists

for dimension in dimensions:
    print(dimension)
print()

#while you cannot modify a tuple, you can redefine it. Ie just reset the varibale name to what u want it
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)
print()