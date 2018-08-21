#!/usr/bin/env python3

words = ['one', 'two', 'three', 'four', 'five']

m = 0
while(m < 5):
    print(words[m])
    m += 1

print()

n = 0
while(n < 5):
    print(words[n], end=' ',flush=True)
    n += 1
print()