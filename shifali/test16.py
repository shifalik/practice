'''
Created on Jan 12, 2018

@author: shifa
'''

#Identity Operators
#Compares Memory Location of Two Objects

#uses is and is not operators


a, b = 20, 20
print("Value of a:", a, "\nId of a is:", id(a) ,"\nValue of b:", b, "\nId of b is:", id(b))

if(a is b):
    print("\na and b have the same identity")
else:
    print("\na and b do not have the same identity")

if( id(a) == id(b)):
    print("a and b have the same identity")
else:
    print("a and b do not have the same identity")

b = 30
print("\nNew Value of b is:", b, "\nId of b is:", id(b))

if(a is not b):
    print("\na and b do not have the same identity")
else:
    print("\na and b have the same identity")
    