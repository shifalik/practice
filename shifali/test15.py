'''
Created on Jan 12, 2018

@author: shifa
'''

#Membership Operators
#Tests for membership in sequences
#Such as strings, lists, tuple

#numerical list
#a = 5
#b = 3
#list1 = [10, 8, 7 , 3, 4, 6]

#word list
#a = 'bobby'
#b = 'cat'
#list1 = ['bobby', 'cat', 'dog', 'pat']

#string
a = 'b'
b = 'c'
list1 = 'banana'

print("Value of a:", a)
print("Value of b:", b)
print("Here are the following members:", list1)

#---------------------------------
#in

if (a in list1):
    print("\na is available")
else:
    print("\na is not available")

#---------------------------------
#not in
    
if (b not in list1):
    print("b is not available")
else:
    print("b is available")

#---------------------------------
#operation and membership
#applies to number list    
#c = b/a

#if (c in list1):
#    print("c is available")
#else:
#    print("c is not available")

