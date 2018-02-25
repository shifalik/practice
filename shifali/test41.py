'''
Created on Feb 7, 2018

@author: shifa
'''

#Trigonometric Functions

#------------------------------------------------
#acos(x) returns the arc cosine of x in radians
#x must be between -1 and 1
#x>1 will generate math domain error

import math

print("acos(0.64):", math.acos(0.64))
print("acos(0):", math.acos(0))
print("acos(-1):", math.acos(-1))
print("acos(1):", math.acos(1))

print()
#------------------------------------------------
#asin(x) returns arc sine of x in radians
#x must be between -1 and 1
#uses import math

print("asin(0.64):", math.asin(0.64))
print("asin(0):", math.asin(0))
print("asin(-1):", math.asin(-1))
print("asin(1):", math.asin(1))

print()
#------------------------------------------------
#atan(x) returns the arc tangent of x in radians
#x must be numeric value
#uses import math

print("atan(0.64):", math.atan(0.64))
print("atan(0):", math.atan(0))
print("atan(10):", math.atan(10))
print("atan(-1):", math.atan(-1))
print("atan(1):", math.atan(1))

#also works like the following:
a = math.atan(2)
print(a)

print()
#------------------------------------------------
#atan2(y,x) returns atan(y/x) in radians
#x,y must be numeric values
#uses import math

print("atan2(-.5,-.5):", math.atan2(-.5,-.5))
print("atan2(.5,.5):", math.atan2(.5,.5))
print("atan2(5,5):", math.atan2(5,5))
print("atan2(-10,10):", math.atan2(-10,10))
print("atan2(10,20):", math.atan2(10,20))

print()
#------------------------------------------------
#cos(x) -- x must be numeric value
#returns cos of x radians
#returns a numeric value between -1 and 1
#it represents the cosine of the angle

#uses import math

print("cos(3):", math.cos(3))
print("cos(-3):", math.cos(-3))
print("cos(0):", math.cos(0))
print("cos(math.pi):", math.cos(math.pi))
print("cos(2*math.pi):", math.cos(2*math.pi))

print()
#------------------------------------------------
#hypot(x,y) returns the Euclidean norm 
#sqrt(x*x + y*y)
#this is the length of vector from origin to point(x,y)

#x,y must be numeric values
#uses import math

print("hypot(3,2):", math.hypot(3,2))
print("hypot(-3,3):", math.hypot(-3,3))
print("hypot(0,2):", math.hypot(0,2))

print()
#------------------------------------------------
#sin(x) returns the sin of x in radians
#x must be numeric value
#returns a numeric value between 01 and 1
#uses import math

print("sin(3):", math.sin(3))
print("sin(-3):", math.sin(-3))
print("sin(0):", math.sin(0))
print("sin(math.pi):", math.sin(math.pi))
print("sin(math.pi/2):", math.sin(math.pi/2))

print()
#-------------------------------------------------
#tan(x) return the tangent of x radians
#x must be a numeric value
#returns a value between -1 and 1
#uses import math

print("tan(3):", math.tan(3))
print("tan(-3):", math.tan(-3))
print("tan(0):", math.tan(0))
print("tan(math.pi):", math.tan(math.pi))
print("tan(math.pi/2):", math.tan(math.pi/2))
print("tan(math.pi/4):", math.tan(math.pi/4))

print()
#------------------------------------------------
#degrees(x) converts angle x from rad to deg
#x must be numeric value
#uses import math

#returns a degree value of an angle

print("degrees(3):", math.degrees(3))
print("degrees(-3):", math.degrees(-3))
print("degrees(0):", math.degrees(0))
print("degrees(math.pi):", math.degrees(math.pi))
print("degrees(math.pi/2)", math.degrees(math.pi/2))
print("degrees(math.pi/4)", math.degrees(math.pi/4))

print()
#-------------------------------------------------
#radians(x) converts angle x from deg to rad
#x must be numeric value
#returns radian value of an angle
#uses import math

print("radians(3):", math.radians(3))
print("radians(-3):", math.radians(-3))
print("radians(0):", math.radians(0))
print("radians(math.pi):", math.radians(math.pi))
print("radians(math.pi/2):", math.radians(math.pi/2))
print("radians(math.pi/4):", math.radians(math.pi/4))

print()
#-------------------------------------------------


