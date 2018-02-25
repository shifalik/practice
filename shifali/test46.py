'''
Created on Feb 9, 2018

@author: shifa
'''
#from filecmp import cmp

#Tuples
#Similar to lists but can't change values
#uses () instead of []

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1,2,3,4,5,6,7)
tup3 = "a","b","c","d"

tup4 = ()       #empty tuple
tup5 = (50,)    #single element

print("Tup1",tup1)
print("Tup2",tup2)
print("Tup3",tup3)
print("Tup4",tup4)
print("Tup5",tup5)
print()
#------------------------------------------------------
print("Accessing Values")
print("Tup1",tup1)
print("Tup2",tup2)

print("tup1[0]", tup1[0])
print("tup2[1:5]", tup2[1:5])

print()
#------------------------------------------------------
print("Updating Tuples")
tup6 = (12,34.56)
tup7 = ('abc', 'xyz')

print('Tup6', tup6)
print('Tup7', tup7)

tup8 = tup6 + tup7
print('Tup8', tup8)

print()
#-------------------------------------------------------
print('Deleting Tuple Elements')
#can not remove individual tuple elements

tup9 = ('physics', 'chemistry', 1997, 2000)
print("Tup9",tup9)

del tup9
#print("After deleting tup9", tup9)
#above will create error as expected 
#since tup9 doesn't exist anymore

print()
#-------------------------------------------------------
print("Basic Tuple Operations")

tup10 = (1,2,3)
print("Tup10", tup10)

tup11 = (4,5,6)
print("Tup11", tup11)

tup12 = ('Hi!',)
print("Tup12", tup12)

print("Length of Tup10",len(tup10))
print("Concatenation", tup10 + tup11)

print("Repetition", tup12 * 4)
print("Membership", 3 in tup10)

for x in tup10: print(x, end=" ")

print()
print()
#-------------------------------------------------------
print("Indexing, Slicing, and Matrixes")

T = ('C++', 'Java', 'Python')

print("T:", T)
print("T[2]:", T[2])
print("T[-2]:", T[-2])
print("T[1:]:", T[1:])

print()
#-------------------------------------------------------
print("Built-in Tuple Functions")
 
print("cmp()")
#compares elements of two tuples
#cmp(tuple1,tuple2)

#if elements are the same type, compare
#----------- ---------------- -------------------- ------
#if elements are not the same type, check to see if they
#are numbers

#if numbers, perform NUMERIC COERCION if necessary and
#compare

#if either element is a number, then the other element
#is larger ---> numbers are the smallest

#otherwise types are sorted alphabetically by name 

#longer tuples is the larger one 
#a tie is 0 if both tuples are the same

tuple1 = (123,'xyz')
tuple2 = (456,'abc')

print("Tuple1:", tuple1)
print("Tuple2:", tuple2)
#cmp(2, 3)
#print cmp(tuple2, tuple1)

tuple3 = tuple2 + tuple1
#print cmp(tuple2, tuple3)

#should get -1 1 -1

print()
#-------------------------------------------------------
print("len(tuple)")
#number of elements are counted

tuple1 = (123, 'xyz', 'zara')
tuple2 = (456, 'abc')

print("Tuple1:", tuple1)
print("Tuple2:", tuple2)

print("First tuple length:", len(tuple1))
print("Second tuple length:", len(tuple2))

print()
#-------------------------------------------------------
print("max(tuple)")
#returns the elements from the tuple with maximum value

tuple1 = ('math', 'che','phy', 'bio')
tuple2 = (456,700,200)

print("Tuple1:", tuple1)
print("Tuple2:", tuple2)

print("Max value element:", max(tuple1))
print("Max value element:", max(tuple2))

print()
#--------------------------------------------------------
print("min(tuple)")
#returns the elements from the tuple with minimum value

tuple1 = ('math', 'che','phy', 'bio')
tuple2 = (456,700,200)

print("Tuple1:", tuple1)
print("Tuple2:", tuple2)

print("Min value element:", min(tuple1))
print("Min value element:", min(tuple2))

print()
#--------------------------------------------------------
print("tuple(seq)")
#converts a list of items into tuples
#seq- this is a tuple to be converted into tuple

list1 = ['math', 'che','phy', 'bio']
print("List1:", list1)

tuple1 = tuple(list1)
print("Tuple Elements:", tuple1)

print()
#---------------------------------------------------------


