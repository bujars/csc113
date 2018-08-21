print("This is today's Lesson 6/6/18")
x = 42
print("value of x is {}".format(x))
n = 42
m = 72
print("value of n is {} and the value of m is {}".format(n,m))


#NOTE for this new version of python 3.6.5 You can do the following
print(f"value of x is {x}") #It's similar to format, except shorter and where the variable is included inside the string statement

print("Hello world %d" %x) #NOTE this also allows us to pass a variable, but it's not as helpful as format -- %d tells the program that a variable is going to be added there. 



#NOTE indentation is meaningful as it connect things togehter
#NOTE def declairs a function


#NOTE these two functions are not called and thus will not print -- Scroll more dwon to see how to call the function
def message():
    print("the message is delivered")

def main():
    print("the message has been sent")
    #call the function message, which will then print its conent
    message()
    print("Great!")

#THIS IS HOW YOU CALL MAIN FUNCTION -- IF you dont call you function then it will ignore all the functions in call
if __name__ == '__main__': main()


""" How to comment out multiple lines 

-- Drag abd select, shift alt a -- 

Like how it currently looks.  """





#Lets now do a conditional. Not paranthesis are not needed

if n < m:
    print('x is smaller')

#You can also write on one single line -- But only works with one command inside
if n < m: print('If-conditional on one line')

#If else conditional
if n>m:
    print('n is greater than m--else')
else:
    print('n is not greater than m--else')


#NOTE here I am changing m = n so that the elif conditional can run
m=n

if n>m:
    print('n is greater than m--elif')
elif n==m:
    print('n is == to m --elif')
else:
    print('n is not greater than m--elif')

#NOTE, setting m back to 72
m = 72


words = ['one', 'two', 'three', 'four', 'five']

#NOTE this is how you make a while look with everything printing next to each other -- That's what flush is for. 
z = 0
while(z < 5):
    print(words[z], end=' ', flush=True)
    z+=1
#I think the problem with why this was infinite was because u had z+-1 not z+=1...I could be wrong though

#NOTE the above isn't working^^ I think its because I included the paranthesis, and z was never updating

""" while z < 5:
    print(words[z], end = ' ', flush=True)
    z+=1 """