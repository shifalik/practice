'''
Created on Jan 26, 2018

@author: shifa
'''

#Iterator and Generator
#Iterator is an object that allows for traversing
#an iterator object implements 2 methods: iter() and next()

#string/list/tuple can be used to create an iterator

list1 = [1,2,3,4]

it = iter(list1)      #builds an iterator object
print(next(it))       #prints next avail element in iterator

#for x in it:
#    print(x, end = " ")

import sys             #module needed this for sys.exit()
while True:
    try:
        print(next(it))
    except StopIteration:
        
        sys.exit()
            
            
