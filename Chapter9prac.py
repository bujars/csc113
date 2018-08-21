class Dog():
    #A simple attempt to model a dog.

    def __init__(self, name, age): #NOTE init function is constructor, def means define a function,
        #this is a "self" function because it accepts self, or an instance as a paramter
        # "Initialzie name and age attributes"
        self.name=name
        self.age = age
    def sit(self):
        #"  Simulate a dog sititng response"
        print(self.name.title() + ' is sitting')
    def roll_over(self):
        print(self.name.title()+' rolled')


#creating instances
joe = Dog('joe', 5)
pug = Dog('pug', 2)

#call funcitons
joe.sit()
joe.roll_over()

#accessing attributes
joe.name


#You cna modify the attributes of an instance directly, or write methods that update attributes in specific ways
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()
    def increment_odometer(self, miles): 
        self.odometer_reading += miles
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
        
my_new_car = Car('audi', 'a4', 2016) 
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#Modifying the attriute
my_new_car.odometer_reading = 23 
my_new_car.read_odometer()

#To make classes more interesting, we can have them have attribites that change overtime
#def update_odometer(self, mileage): #added to class
#"""Set the odometer reading to the given value.""" self.odometer_reading = mileage

#Showing how you can't go backwards on an odometer
my_new_car.update_odometer(20) 
my_new_car.read_odometer()


#Showing an incremenet
my_used_car = Car('subaru', 'outback', 2013) 
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500) 
my_used_car.read_odometer()
my_used_car.increment_odometer(100) 
my_used_car.read_odometer()