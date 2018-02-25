'''
Created on Jan 12, 2018

@author: shifa
'''

#Bitwise Operators

a, b, c = 20, 15, 0
print("Value of a is:", a,"\nValue of binary a is:", bin(a))
print("Value of b is:", b,"\nValue of binary b is:", bin(b))
print("Value of c is:", c,"\nValue of binary c is:", bin(c))

c = a & b
print("\nResult of AND operator:", c, "\nResult In Binary:", bin(c))

c = a | b
print("\nResult of OR operator:", c, "\nResult In Binary:", bin(c))

c = a ^ b
print("\nResult of XOR operator:", c, "\nResult In Binary:", bin(c))

c = ~a
print("\nResult of ONES COMPLEMENT operator:", c, "\nResult In Binary:", bin(c))

c = a << 2
print("\nResult of LEFT SHIFT operator:", c, "\nResult In Binary:", bin(c))

c = a >> 2
print("\nResult of RIGHT SHIFT operator:", c, "\nResult In Binary:", bin(c))
