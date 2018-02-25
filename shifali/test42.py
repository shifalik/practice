'''
Created on Feb 7, 2018

@author: shifa
'''

# STRINGS
# python treats single quotes same as double quotes

#-----------------------------------------
# accessing values in strings

var1 = 'Hello World'
var2 = 'Python Programming'

print("var1[0]:", var1[0])
# prints 1st letter

print("var2[1:5]:", var2[1:5])
# prints from 1st letter to 4th letter

print("var1[:6]:", var1[:6])
# prints the first word --> Hello( )
#first 5 letters

print()
#------------------------------------------
# updating strings

var1 = 'Hello World'
print("Updated String:", var1[:6] + 'Python')
# concatenates Hello( )with new word 

print()
#------------------------------------------
# Special String Operations

a = 'Hello'
b = 'Python'

print("Concatenation:", a + b)
print("Repetition:", a * 2)

print("Slice:", a[1])
print("Range Slice:", a[1:4])

print("Membership:", 'H' in a)
print("Membership:", 'M' not in a)

print("Raw String:", r'\n')
print("Raw String:", R'\n')
# suppresses actual meaning of escape characters

print()
#----------------------------------------------------
# string formatting operator %
# coolest feature**

print("My name is %s and weight is %d kg!" % ('Shifali' , 25))
# %s is string conversion via str() prior to formatting
# %d is signed decimal integer

#order matters

print()
#----------------------------------------------------
# Triple Quotes
# allows strings to span multiple lines

para_str = """hello there 
how do (\n) you do? (\t) very well.
"""
print(para_str)
# (\t) is tab

print()
#----------------------------------------------------
# raw strings
print('C:\\nowhere')        
print(r'C:\\nowhere')  # raw string ---> r'expression'

