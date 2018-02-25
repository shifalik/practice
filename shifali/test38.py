'''
Created on Jan 30, 2018

@author: shifa
'''

#number type conversion

x = 4.234 
y= 1.2

print("Value of x is:", x,"\nValue of y is:", y)

#convert into plain integer
print("\nX in integer format is:        ",int(x))

#convert into a floating-point number
print("X in float format is:          ",float(x))

#convert to a complex number with real part x and imaginary
#part zero
print("X in complex format is:       ",complex(x))

#convert x and y to a complex number with real part x
#and imaginary part y. x and y are numeric expressions
print("X and Y in complex format are:",complex(x,y))

