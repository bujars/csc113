#working with files/accessing files through python
#p.opne(filename, mode) #mode are following
#'r' when the fill will only be read
#'w' for only writing, creating a new file (an existing filr eith the same name)
#'a' opens the file for appending; any data written to the file is automaticaly added to the end of the file
#'r+' opens the file for both reading and writing
#when mode is not giveb, 'r' is assumed

f = open('workfile.txt', 'w') #created a file and write in it use w 
f.closed #how to check if a file is opened or closed
f.close() #how to close a file
f.closed


f.open('workfile.py' 'w')
f.close()

f= open('workfile.txt')
f.read() #prints empty string because nothing is in the file


#use the with keyword for file objects.
#The advantage: file is properly closed after its suite finishes
#even if an excepion is raised at some point

with open('workfile.txt') as f:
    read_data=f.read()
f.closed # note its true becasue its automaticaly close wiht the 'with' keyword

type(read_data) 

#After a file object is closed,either by a with statement or by calling f.close()
#attempts to use the file object with automatically fail.
f.close()
#f.read() #.....error

#f.write(string) write the contenets of string to the file, returning the number of characers
#the file must be open to write
#the file must be close to see the change
f.closed
f=open('workfile.txt', 'w')
f.write('This is a test\n')
f.close()
f.closed

#everytimme you call mode 'w' , it overwrite sthe text
f=open('workfile.txt', 'w')
f.write('test2\n')
#f.read() --error because the file is open in w mode. and cannot be read
f.close()


#Lets add stuff without rewriting

f = open('workfile.txt', 'a')
f.write('This is the second test\n')
f.close()

f = open('workfile.txt')
f.readline()
f.readline()
f.read() #doesn't do anything because theres nothing left to read
f.close()


f = open('workfile.txt')
f.read() #outputs everything as it reads everything. It prints it as one string with everything appeneded to one another
#not a prefered format
f.close()

#Can print each line one-by-one

f = open('workfile.txt')
for line in f:
    print(line, end='')

f.close()




with open('workfile.txt', 'r+') as f:
    f.read()
    f.write('third line')
    f.read()
f.close()

f = open('workfile.txt')


#note you cannot write a tuple into a file, must convert it into a string
value = (42)
s = str(value)

f = open('workfile.txt', 'a')
f.write(s)
f.close()

#f.seek(offset, from_what) 
#the potition is computed from adding offset to a reference point
# the reference point is selected by the from_what argument
#A frome_what value of 0 measures from the beginning of the file
#1 uses the current file position
#and 2 uses the end of the fole as a reference point
#from_what file can be ommited and defaults to 0, using the beginning of the file a sa reference

f = open('workfile1.txt', 'w')
f.close()

f = open('workfile1.txt', 'rb+')# rb+ mode lets you read/write and seek in a file
f.write(b'0123456789abcdef') #b stands from byte
f.close()

f = open('workfile1.txt', 'rb+')

#note 5 is position -- think of index, not necessarily like finding the number 5
f.seek(5) #Go to the 6th byte in the file -- since starting from 0
f.read(1) #the one means the byte from the given seek position 
f.seek(7)
f.read(1) 
f.read(2) #number of bytes you want to read, from the current position
f.read(3)



f.seek(5,2) #prints nothing because the 2 goes to the end of the file when read is called
f.read(1)

f.seek(5)
f.read() #prints everything starting at 5

f.seek(5,2)
f.read() 
#again prints nothing because the 2 sends it to the end of the file. 


#Let's say you want a nuumber that is at the end or starting from the end
f.seek(-3,2) #Must have the 2 to let the computer know that you are from the end
f.read()