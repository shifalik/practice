'''
Created on Jan 10, 2018

@author: shifa
'''

#tuples---read only lists(no edits)
#parentheses used

tuple0 = ('def', 45, 34.09, 'santa')
tuple1 = ('ijk', 56.7, 32.0, 'clause')


print(tuple0)
print(tuple1)
print("\n")

print(tuple0[0])         #1st element
print(tuple0[1:3])       #2nd to 3rd print
print(tuple0[2:])        #from 3rd to end
print(tuple1 * 2)        #repetition 
print(tuple0 + tuple1)   #added concatenation 
print("\n")
print(tuple0 + tuple1 + tuple0)
print(tuple0 + tuple1 * 2)

#tuple[3] = 100          #wont work cant alter tuple, only lists

t = tuple0.__add__(tuple1)
print("new:>> ",t)

