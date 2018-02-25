'''
Created on Jan 18, 2018

@author: shifa
'''

#Operators Precedence Example

a, b, c, d = 20, 10, 15, 5
print("a:%d b:%d c:%d d:%d" % (a,b,c,d))

e = (a + b) * c / d
print("\nValue of (a+b)*c /d is:", e)
#(30 * 15)/5

e = ((a + b) * c) / d
print("Value of (a+b)*c) /d is:", e)
#(30 * 15)/5

e = (a + b) * (c / d)
print("Value of (a+b) * (c/d) is:", e)
#30 * 3

e = a + (b * c) / d 
print("Value of a+(b*c) /d is:", e)
#20 + (150 /5)


