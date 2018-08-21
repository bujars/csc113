x = range(5)
for i in x:
    print('i is {}'.format(i))

x = range(5, 10)
for i in x:
    print('i is {}'.format(i))

x = range(5,50, 10)
for i in x:
    print('i is {}'.format(i))

#range is immutable
x = range(5)
x=list(range(5))
x[2]=42
for i in x:
    print('i is {}'.format(i))
