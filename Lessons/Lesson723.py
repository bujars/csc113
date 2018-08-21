#Introduction to Matplotlib

import matplotlib #installation:pip install matplotlab

#for exaple of a line plot:
from numpy import sin #numpy for mathematical operation
from matplotlib import pyplot
x = [x*0.1 for x in range(100)] #consistent interval for the x-axix
y = sin(x)
pyplot.plot(x,y) #create line plot
pyplot.show()


#example of a bar chart
from random import seed
from random import randint
from matplotlib import pyplot
seed(1) #initialize the random number generator
x = ['red', 'green', 'blue'] #names for categories
y = [randint(0,100), randint(0,100), randint(0, 100)]
pyplot.bar(x,y)
pyplot.show()

#example of a histogram plot
from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot 
seed(1) # seed the radom number generated
x = randn(1000) #random numbers drawn from a Gausteian Distribution
pyplot.hist(x)
pyplot.show()

#Boxplot
x = [rand(1000), 5 *randn(1000), 10 *randn(1000)]
#create box and whisker plot
pyplot.boxplot(x)
#show line plot
pyplot.show()


#Scatterplot
#first variable
x = 20*randn(1000)+100
#second variable
y = x + (10*randn(1000) + 50)
#create scatter plot
pyplot.scatter(x , y)
#show line plot
pyplot.show()


##Started visualation 2 file, but missed intro .. --How to plot a temperature graph. 
from matplotlib 


import numpy as numpy
import cv2 #how to install cv2

#Load an color image in grayscale
img = cv2.imread('cat1.jpg', 0) #Makesure you have this image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
