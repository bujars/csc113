#Only immutable data types can be used as keys,
#i.e. no lists or dictionaries can be used 
#If you use a mutable data type as a key, you get an error message:
#dic = { [1,2,3]:"abc"}  #error

#Tuple as keys are okay, because they are immutable:
d = { (1,2,3):"abc", 3.1415:"abc"}
d
d[(1,2,3)]
d[3.1415]

#no restrictions for the values: immutable or mutable 

#Multi dimensional dictionaries
D1 = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}

D2 = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}

dictionaries = {"german dictionary" : D1, "french dictionary" : D2 }

dictionaries

dictionaries["french dictionary"]

dictionaries["french dictionary"]["blau"]

dictionaries["german dictionary"]

dictionaries["german dictionary"]["green"]
dictionaries["german dictionary"]["blue"]


#membership for keys 
'blue' in D1 #asking the membership of  a key 
'blau' in D1
'blau' in D2

#pop, 
capitals = {"Springfield":"Illinois", "Augusta":"Maine", "Boston": "Massachusetts", "Lansing":"Michigan", "Albany":"New York", "Olympia":"Washington", "Toronto":"Ontario"}
capitals.pop("Springfield") #returns the value of this key, at the item will be removed
"Springfield" in capitals
if "Springfield" in capitals: print(capitals["Springfield"])
if "Albany" in capitals: print(capitals["Albany"])

#popitem : doesn't take any parameter 
#: removes and returns an arbitrary (key,value) pair as a 2-tuple
(city, state) = capitals.popitem()
type(capitals.popitem())

#method get 
proj_language = {"proj1":"Python", "proj2":"Perl", "proj3":"Java"}
proj_language["proj1"]
proj_language["proj4"]
proj_language.get("proj2")
proj_language.get("proj4")
print(proj_language.get("proj4"))

#copy()
proj_language = {"proj1":"Python", "proj2":"Perl", "proj3":"Java"}
D = proj_language.copy()
D
proj_language["proj4"]="c++"
print(D)
print(proj_language)

#copy: If a value is a complex data type like a list, for example, in-place changes in this object have effects on the copy as well
trainings = { "course1":{"title":"Python Training Course for Beginners", 
                         "location":"Frankfurt", 
                         "trainer":"Steve G. Snake"},
              "course2":{"title":"Intermediate Python Training",
                         "location":"Berlin",
                         "trainer":"Ella M. Charming"},
              "course3":{"title":"Python Text Processing Course",
                         "location":"München",
                         "trainer":"Monica A. Snowdon"}
              }
trainings2 = trainings.copy()
trainings["course2"]
trainings["course2"]["title"]
trainings["course2"]["title"] = "Perl Training Course for Beginners"
print(trainings2)

#Everything works the way you expect it, if you assign a new value, i.e. a new object, to a key:
trainings = { "course1":{"title":"Python Training Course for Beginners", 
                         "location":"Frankfurt", 
                         "trainer":"Steve G. Snake"},
              "course2":{"title":"Intermediate Python Training",
                         "location":"Berlin",
                         "trainer":"Ella M. Charming"},
              "course3":{"title":"Python Text Processing Course",
                         "location":"München",
                         "trainer":"Monica A. Snowdon"}
              }

trainings2 = trainings.copy()

trainings["course2"] = {"title":"Perl Seminar for Beginners",
                         "location":"Ulm",
                         "trainer":"James D. Morgan"}
print(trainings2["course2"])

#Merging Dictionaries
knowledge = {"Frank": {"Perl"}, "Monica":{"C","C++"}}
knowledge2 = {"Guido":{"Python"}, "Frank":{"Java", "Python"}}
knowledge.update(knowledge2)
knowledge

knowledge = {"Frank": [1,2,3], "Monica":{"C","C++"}}
knowledge2 = {"Guido":{"Python"}, "Frank":[3,4]}
knowledge.update(knowledge2)
knowledge

knowledge = {"Frank": 1, "Monica":{"C","C++"}}
knowledge2 = {"Guido":{"Python"}, "Frank":2}
knowledge.update(knowledge2)
knowledge


#lists and dictionaries 
w = {"house":"Haus", "cat":"", "red":"rot"}
items_view = w.items()
items = list(items_view)
items

keys_view = w.keys()
w.keys()
keys = list(keys_view)
keys

values_view = w.values()
values = list(values_view)
values

values_view
items_view
keys_view

#Turn Lists into Dictionaries
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]

country_specialities_iterator = zip(countries, dishes)
country_specialities_iterator

country_specialities = list(country_specialities_iterator)
print(country_specialities)

country_specialities_dict = dict(country_specialities)
print(country_specialities_dict)

#a list of tuples can be converted to a dictionary, in one step 
t=[('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]
dict(t)

A=['alice','bob','tom']
B=[20,25,30]
list(zip(A,B))
D=dict(list(zip(A,B)))
D

#quicker way:
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
z=zip(countries, dishes)
dict(z)

A=[(1,2),(3,4)]
dict(A)

A=[[1,2],[3,4]] #List of lists can be converted to a dictionary, directly
dict(A)

#special cases
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
len(dishes)
countries = ["Italy", "Germany", "Spain", "USA","Switzerland"]
len(countries)

country_specialities = list(zip(countries, dishes))
country_specialities 
country_specialities_dict = dict(country_specialities)
print(country_specialities_dict)

#one step:
country_specialities_dict = dict(zip(["pizza", "sauerkraut", "paella", "hamburger"], ["Italy", "Germany", "Spain", "USA"," Switzerland"]))
print(country_specialities_dict)

