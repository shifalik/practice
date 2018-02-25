'''
Created on Feb 8, 2018

@author: shifa
'''

# Lists 
# They are sequences
# NOTE: items in list don't have to be same data type

#--------------------------------------------------------
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
print("List1:", list1, "\nList2:", list2, "\nList3:", list3)
print()
#--------------------------------------------------------
print("Accessing values in list.")
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
print()
#--------------------------------------------------------
print("Updating Lists")
print("Value available at index 2: ", list1[2])
list1[2] = 2001
print("New value available at index 2: ", list1[2])
print()
#--------------------------------------------------------
print("Delete List Elements")
print(list1)
del list1[2]
print("After deleting value at index 2:\n", list1)
print()
#--------------------------------------------------------
print("Basic List Operations")

a = [1, 2, 3]
b = [4, 5, 6]
c = ['Hi!']

print("List a:", a, "\nList b:", b, "\nList c:", c)
print()
print("Length of a:", len(a))
print("Concatenation of a and b:", a + b)
print("Repetition of c:", c * 4)
print("Membership of 3 in a:", 3 in a)

# for loop to print all values of a
print("Printing values of a using for loop:")
for x in a:
    print(x, end=' ')      
    
# end=' ' gives it space while printing instead of 
# printing on a new line
print()
print()
#--------------------------------------------------------
print("Indexing, Slicing, and Matrixes")

L = ['C++', 'Java', 'Python' , 'C#', 'Ruby']   
print("List L:", L)
print()

print("Offsets start at 0:")
print("L[2]:", L[2])      
   
print("Negative: count from the right:")   
print("L[-2]:", L[-2])       
#counts from backwards for L[-2]

print("Slicing fetches sections:")
print("L[1:]:", L[1:])      

print()
#--------------------------------------------------------
print("BULIT IN FUNCTIONS AND METHODS")
#--------------------------------------------------------
print()
print("len(list)")

list1 = ['physics', 'chemistry', 'math']
print("list1: ", list1)
print("Length of list1: ", len(list1))

list2 = list(range(5))  # creates list of numbers between 0-4
print("list2: ", list2)
print("length of list2: ", len(list2))

print()
#--------------------------------------------------------
print("max(list)")
# max valued element is to be returned

list1, list2 = ['C++', 'Java', 'Za', 'Zb' ,'Python', 'Alphabetical'], [456, 700, 200]
#max prints higher valued letter in beginning

print("list1:", list1, "\nlist2", list2)
print("Max value element from list1:", max(list1))
print("Max value element from list2:", max(list2))

#--------------------------------------------------------
print("min(list)")
# using above lists

print("Min value element from list1:", min(list1))
print("Min value element from list2:", min(list2))

print()
#--------------------------------------------------------
print("list(seq)")

# takes sequence types and converts them to lists
# used to convert tuple or string into list
# tuple uses (), lists use []

aTuple = (123, 'C++', 'Java', 'Python')
list1 = list(aTuple)
print("List elements from tuple:", list1)

str1 = "Hello World"
list2 = list(str1)
print("list elements from string:", list2)

print()
#--------------------------------------------------------
print("METHODS")
#--------------------------------------------------------
print()
print("list.append(obj)")
# does not return value but updates list

list1 = ['C++', 'Java', 'Python']
print("list1:", list1)

list1.append('C#')
print("updated list:", list1)

print()
#--------------------------------------------------------
print("list.count(obj)")
# returns count of how many times obj occurs in list

aList = [123, 'xyz', 'zara', 'abc', 123]
print("aList:", aList)

print("Count for 123:", aList.count(123))
print("Count for zara:", aList.count('zara'))
# tested: if there are no values then it will return 0

print()
#--------------------------------------------------------
print("list.extend(seq)")
# appends the contents of seq to list
# does not return any value but adds the content 
# to existing list

list1 = ['physics', 'chemistry', 'math']
list2 = list(range(5))
print("list1:", list1)
print("list2:", list2)

list1.extend(list2)
print("Extended List:", list1)

#different from concatenation because in concatenation you
#need to store a + b into c
#here we don't need to because list1 is extended

print()
#--------------------------------------------------------
print("list.index(obj)")
# returns lowest index in list that obj appears
# raises exception if object not found

list1 = ['physics', 'chemistry', 'math']
print("list1:", list1)

print("Index of chemistry:", list1.index("chemistry"))
# print("Index of C#", list1.index("C#"))
# throws exception like it should

print()
#--------------------------------------------------------
print("list.insert(index, obj)")
# inserts object into list at offset index
# index is where object obj is needed to be inserted
# obj is what is going in the list

list1 = ['physics', 'chemistry', 'math']
print("list1:", list1)

list1.insert(1, 'biology')
print("Final List: ", list1)

# all else gets pushed down the list
print()
#--------------------------------------------------------
print('list.pop(obj = list[-1]')
# removes and returns last object from the list
# obj is optional parameter, can give index of object 

list1 = ['physics', 'biology', 'chemistry', 'math']
print("list1:", list1)

list1.pop()  # takes off last element
print("list1 now:", list1)

list1.pop(1)  # takes off list1[1] element
print("list1 now:", list1)

print()
#--------------------------------------------------------
print('list.remove(obj)')

list1 = ['physics', 'biology', 'chemistry', 'math']
print("list1:", list1)

list1.remove('biology')
print("list1 now:", list1)

list1.remove("math")
print("list1 now:", list1)

print()
#--------------------------------------------------------
print("list.reverse()")
# reverses objects of list in place

list1 = ['physics', 'biology', 'chemistry', 'math']
print("list1:", list1)

list1.reverse()
print("reversed list1:", list1)

print()
#--------------------------------------------------------
print("list.sort([func])")
# sorts objects of list

list1 = ['physics', 'biology', 'chemistry', 'math']
print("list1:", list1)

list1.sort()
print("sorted list1:", list1)

print()
#--------------------------------------------------------

