#Only immutable data types can be used as jeys
#o lists or dicitonaires can be used as keys


#dic = {[1,2,3]L"abc"} #error -- Key cannot be mutable 
d = {(1,2,3):'abc', 3.145:'abc'} #since the key is a tuple, it is immutable and thus produced no error 
print(d)

#no restrictions for the values: immutable or mutable

#Multi dimensional dictionaries

D1 = {'red' : 'rot', 'green': 'grun', 'blue': 'blau'} #english --german
D2 = {'rot':'rouge','grun':'vert', 'blau':'bleu'}
dictionaries = {'german dictionary':D1, "french dictionary" : D2}
print(dictionaries)


#Can ask for certain parts of the dictionary of dictionaries, by "key" ofc -- ie blau or green
dictionaries['french dictionary']['blau']

dictionaries['french dictionary']

dictionaries['german dictionary']['green']


#membership for keys
'blue' in D1 #asking the membership of a key -- Type out in python terminal, doesn't run when u use mouse commands
'blau' in D1
'blau' in D2


#pop
capitals = {"Springfield":'Illinois', 'Albany':'New York', 'Augusta':'Maine'}
capitals.pop("Springfield") #returns the vlaue of this key, and the item will be removed
'Springfield' in capitals
if 'Springfield' in capitals: print(capitals['Springfield'])

if 'Albany' in capitals: print(capitals['Albany'])

#popitem:doesn't take any parameters
#:removes ad returns arbitrary (kay,value) pair as a 2-tuple
(city,  state) = capitals.popitem()
type(capitals.popitem())

#method get
proj_language = {'proj1':'python', 'proj2':'Perl','proj3':'Java'}
proj_language['proj1']
proj_language['proj4'] ##error cannot access anything here
proj_language.get('proj2')
proj_language.get('proj4')
print(proj_language.get('proj4'))

#copy()
D = proj_language.copy()
D #note how it makes a copy

proj_language.append(['proj4':'C++'])
proj_language
D

#copy: If a value is a complex data type like a list, in place changes can occur
trainings = {"course 1":{"title":'bujar',"subject":'python'}, 'course 2':{'title':'lol', 'subject':'c++'}}
trainings2 = trainings.copy();
trainings2
trainings['course 2']
trainings['course 2'] = {'title':'l', 'subject':'Java'} #note it changed for this dictionary
trainings
trainings2 #does not change for this dictionary

#Merging Dictionaries -- It cannot merge second dimension dictionaries -- Look at frank 
knowledge = {'Frank':{'Perl'}, 'Monica':{'C', 'C++'}}
knowledge2 = {'Bujar':{'Java'}, 'Frank':{'Ruby'}}
knowledge.update(knowledge2)
knowledge #combines knowledge2 to knowledge1 --Frank goes from Perl to Ruby 


#NOTE how the values must be dictionaries or of some other type -- check her notes, as if they are integers, it will not uupdate/merge the dictionaries


#lists and dictionaries
w = {'pot':'pan', 'spoon':'fork'}
itmes_list = w.items()
itmes_list
items = list(itmes_list)
items


#Turning Lists into Dictionaries
dishes = ['pizza', 'paella', 'hamburger']
countries = ['italy', 'Spain', 'USA']

country_specialities_iterator = zip(countries, dishes) #zip is another class and it merges two things into a zip format 
#--Note if you don't have same size it will just ignore -- see down
country_specialities_iterator

country_specialities = list(country_specialities_iterator)
print(country_specialities)

country_specialities_dict = dict(country_specialities)
print(country_specialities_dict)

#a list of tuples can be converted to a dictionary, in one step
t = [('italy', 'pizza'), ('Spain', 'paella'), ('USA', 'hamburger')]
dict(t) 
t = dict(t) 
t

A=['alice','bob','tom']
B=[20,25, 30] #Note if we remove 30, tom will not appear in the list/dictionary 
list(zip(A,B))
dict(list(zip(A,B)))

#A quicker way
dishes = ['pizza', 'paella', 'hamburger']
countries = ['italy', 'Spain', 'USA']
z = zip(countries, dishes)
dict(z) #we can directly call dict on a zip. WE don't necessarily have to convert to a list. List helps us see what is going on. 
