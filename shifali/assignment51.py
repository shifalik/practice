'''
Created on Feb 25, 2018

@author: shifa
'''
list1 = [100, 24, 23, 76, 56, 22, 10, 96]
list2 = [100, 34, 75, 3, 56, 33, 23, 86]
 
list3 = list1 + list2
print("List3(unsorted):", list3)
 
count = len(list3)
 
list4 = []
i = 0
while count != 0:
    a = min(list3)
    list4.insert(i, a)
    b = list3.index(a)
    list3.pop(b)
    count -= 1
    i += 1
     
print("List4:          ", list4)
 
print()