'''
Created on Jan 30, 2018

@author: shifa
'''

#generator
#function that produces or yields a sequence of values 
#using yield method

#when generator function is called returns a generator 
#object without even beginning execution of the function

#below generates an iterator for all FIbonacci numbers

import sys
def fibonacci(n):   #generator function
    a, b, counter = 0,1,0
    while True:
        if(counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(5)   #f is the iteration object 

while True:
    try:
        print( next(f), end= " ")
    except StopIteration:
        sys.exit()
        
        