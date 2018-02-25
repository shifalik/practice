'''
Created on Jan 30, 2018

@author: shifa
'''
#mathematical functions
#--------------------------------------------------
#absolute value of x

print("This returns the absolute value of x.")
print("abs(-45):", abs(-45))
print("abs(100.12):", abs(100.12))

print()
#--------------------------------------------------
#ceiling of x, returns smallest integer not less than x

import math

print("This returns the smallest integer not less than x.")
print("math.ceil(-45.17):", math.ceil(-45.17))
print("math.ceil(100.12):", math.ceil(100.12))
print("math.ceil(100.72):", math.ceil(100.72))
print("math.ceil(math.pi):", math.ceil(math.pi))

print()
#--------------------------------------------------
#cmp(x,y) ===== return (x>y)-(x<y)
#-1 if x < y
#0 if x == y
#1 if x > y

x, y = 100, 10
print((x>y)-(x<y))

print()
#--------------------------------------------------
#exponent ---> e^x
#using import math

print("This returns the e^x value.")
print("math.exp(-45.17):", math.exp(-45.17))
print("math.exp(100.12):", math.exp(100.12))
print("math.exp(100.72):", math.exp(100.72))
print("math.exp(math.pi):", math.exp(math.pi))

print()
#--------------------------------------------------
#fabs() ---> absolute value of x
#works on float and integer
#uses import math
#abs() also works with complex but fabs() does not

print('This is gives absolute value of int or float.')
print("math.fabs(-45.17):", math.fabs(-45.17))
print("math.fabs(100.12):", math.fabs(100.12))
print("math.fabs(100.72):", math.fabs(100.72))
print("math.fabs(math.pi):", math.fabs(math.pi))

print()
#--------------------------------------------------
#floor(x) -->gives the largest integer not greater than x
#uses import math

print("This returns the largest integer not greater than x.")
print("math.floor(-45.17):", math.floor(-45.17))
print("math.floor(100.12):", math.floor(100.12))
print("math.floor(100.72):", math.floor(100.72))
print("math.floor(math.pi):", math.floor(math.pi))

print()
#--------------------------------------------------
#log function --> returns the natural logarithm of x
#for x > 0
#uses import math

print("This returns the log value of x.")
print("math.log(100.12):", math.log(100.12))
print("math.log(100.72):", math.log(100.72))
print("math.log(math.pi):", math.log(math.pi))

print()
#--------------------------------------------------
#log10() --> returns base 10 logarithm of x for x > 0
#uses import math

print("This returns the base 10 log of x.")
print("math.log10(100.12):", math.log10(100.12))
print("math.log10(100.72):", math.log10(100.72))
print("math.log10(119):", math.log10(119))
print("math.log10(math.pi):", math.log10(math.pi))

print()
#--------------------------------------------------
#max() method returns the largest of its arguments
#the value closest to positive infinity

print("Max gives the highest value.")
print("max(80,100,100):", max(80,100,1000))
print("max(-20,100,400):", max(-20,100,400))
print("max(-80,-20,-10):", max(-80,-20,-10))
print("max(0,100,-400):", max(0,100,-400))

print()
#--------------------------------------------------
#min() finds the smallest values closet to 
#negative infinity

print("Min find the smallest value.")
print("min(80,100,100):", min(80,100,1000))
print("min(-20,100,400):", min(-20,100,400))
print("min(-80,-20,-10):", min(-80,-20,-10))
print("min(0,100,-400):", min(0,100,-400))

print()
#--------------------------------------------------
#modf()
#returns the fractional and integer parts of x in a
#two item tuple; integer returned as float

#uses import math

print("Returns the fractional and integer parts of x.")
print("math.modf(100.12):", math.modf(100.12))
print("math.modf(100.72):", math.modf(100.72))
print("math.modf(119):", math.modf(119))
print("math.modf(math.pi):", math.modf(math.pi))

print()
#--------------------------------------------------
#pow() method returns the value of x^y
#uses import math

print("Returns x^y.")
print("math.pow(100,2):", math.pow(100,2))
print("math.pow(100,-2):", math.pow(100,-2))
print("math.pow(2,4):", math.pow(2,4))
print("math.pow(3,0):", math.pow(3,0))

print()
#--------------------------------------------------
#round(x,[,n])
#x is rounded to n digits from decimal point
#python rounds away from 0
#default n is 0

print("Rounding where n is the digits from decimal point.")
print("round(70.23456):", round(70.23456))
print("round(56.659,1):", round(56.659,1))
print("round(80.264,2):", round(80.264,2))
print("round(100.000056,3):", round(100.000056,3))
print("round(-100.000056,3):", round(-100.000056,3))

print()
#--------------------------------------------------
#square root
#uses import math
#returns square root for x 
#x>0

print("Square Root for x > 1.")
print("math.sqrt(100):", math.sqrt(100))
print("math.sqrt(7):", math.sqrt(7))
print("math.sqrt(math.pi):", math.sqrt(math.pi))

