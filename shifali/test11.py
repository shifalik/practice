'''
Created on Jan 12, 2018

@author: shifa
'''

#Comparison Operators

a = 5
b = 10

print("Value of a:",a,"\nValue of b:",b,"\n")

print("Performing the SWAP")
a,b = b,a

print("New value of a:",a,"\nNew value of b:",b,"\n")


#-----------------------------------------------
print("Test One (==)")                              #Equal

if (a==b):
    print("a is equal to b")
else:
    print("a is not equal to b")

#-----------------------------------------------
print("\nTest Two (!=)")                            #NotEqual

if (a!=b):
    print("a is not equal to b")
else:
    print("a is equal to b")

#-----------------------------------------------
print("\nTest Three (>)")                           #Greater Than

if (a>b):
    print("a is greater than b")
else:
    print("a is not greater than b")
    
#-----------------------------------------------
print("\nTest Four (<)")                            #Less Than

if (a<b):
    print("a is less than b")
else:
    print("a is not less than b")
    
#-----------------------------------------------
print("\nTest Five (>=)")                           #Greater Than or Equal To

if (a>=b):
    print("a is greater than or equal to b")
else:
    print("a is not greater than or equal to b")

#-----------------------------------------------
print("\nTest Six (<=)")                            #Less Than or Equal To

if (a<=b):
    print("a is less than or equal to b")
else:
    print("a is not less than or equal to b")
    
#-----------------------------------------------







