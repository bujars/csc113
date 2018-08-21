#!/usr/bin/env python3

#NOTE to comment stuff use # 


#NOTE This prints Hellow World. Notice, the function is called print and the string can be in single quotations. 
print('Hello, World. Single Quotes')

print("Hello, WOorld. Double Quotes")

#NOTE There are no semi-colons at the end of statements. 

print('Trying out how to use either quotes within one another.')
print("'Hello'")
print('"Hello"')
print('Either works')

print('It\'s a lovely day')
print('To include the \' in the printing, you must do \ \' ')


print('something else')


#NOTE how the below print next to each other. This has to do with the function called flush, which flushes the words together. 
# The end='' tells the program to keep a space between them, to end the first print with a space and then continue the next print. 
# Without it, it just prints the next print on the next line. 


print('Hello, World.', end=' ', flush=True)
#print('Hello, World.', end= 'a', flush=True)

print('something else')


