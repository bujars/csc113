#!/usr/bin/env python3

"""  
def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            print(f'{n} is not prime')
            return False
    else:
        print(f'{n} is prime')
        return True
isprime(5)
isprime(10)
 """


""" 
def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def list_primes():
    for n in range(100):
        if isprime(n):
            print(n, end=' ', flush=True)

    print()

list_primes() """