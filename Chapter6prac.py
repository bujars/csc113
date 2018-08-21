#Dictionaries allow you to store multiple things realting to one thing

alien_o = {'color': 'green', 'points': 5} #Notice how an alien can have a color, and a vlaue of points

#to print the color
print(alien_o['color'])
print(alien_o['points'])

#A dictionary is a collection of key-value pairs. 
# Each key is connected to a specific value, and the key is used to access the value.  
# Keys and values are conected by a colon : 

new_points = alien_o['points']
print("You just earned " + str(new_points)+ ' points!')

#Dictionaries are dynamic structures. You can add new key-value pairs at any times
alien_o['x-position'] = 0 #how you add 
alien_o['y-position'] = 25
print(alien_o) #Notice this prints the whole dictionary 

#Python doesn't care about the order of the key/value, onl that each key/value is connected to each other

#Dictionares can start of empty

alien_o ={}
alien_o['color']='green'
alien_o['points'] = 5
print(alien_o)

#To modify a value in a dictionary, 
# give the name of the dictionary with the key in square brackets and then the new value you want associated with that key. 

alien_o['color'] ='blue'
print(alien_o)

#Let's track the position (example postion) of the aline

alien_o['speed']='medium'
alien_o['x']=0
alien_o['y']=25
print(alien_o)
#move it to the right, determine how far

if alien_o['speed']=='slow':
    add = 1
elif alien_o['speed']=='medium':
    add=2
else:
    add = 3
#new pos is old pos plus add
alien_o['x'] = alien_o['x']+add
print("New pos x is: " + str(alien_o['x']))

#REMOVING key value pairs
#use delete function del

del alien_o['points']
print(alien_o)

#Making a dictionary, via looking pretty
favorite_languages = {
    'jen': 'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
    }
print(favorite_languages)