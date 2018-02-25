'''
Created on Jan 10, 2018

@author: shifa
'''


#lists
#can include various types
#use of brackets

list1 = [ 'a', 124, 54.0, 'abc']
list2 = [ 78, 54.32, 'efg']

print(len(list1))
print(list1)
print(list2)
print("\n")

print(list1[0])        #print first element from list 
print(list1[1:3])      #print starting from the 2nd to the 3rd
print(list1[2:])       #print starting from 3rd till end
print(list2 * 2)       #repeated twice
print(list1 + list2)   #concatenation added 

list2[2] = 'def'       #can not update future value like list2[3] ~out of range~ 
print(list2)

list1.insert(2, 5)    #everything shifts forward
print(list1)

print(list2[:2])


