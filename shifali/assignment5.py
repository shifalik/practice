# '''
# Created on Feb 17, 2018
# 
# @author: shifa
# '''
# 
# # merge to sorted lists
# # learn how to sort
# 
# #---------------------------------------------
# #how to sort merged list
# 
# list1 = [100,24,23,76,56,22,10,96]
# list2 = [100,34,75,3,56,33,23,86]
# list3 = list1 + list2
# list3.sort()
# print("List3 sorted with just one function:")
# print(list3)
# 
# print()
# #---------------------------------------------
# # using min()/insert()/index()/pop() to sort 
# 
# list1 = [100, 24, 23, 76, 56, 22, 10, 96]
# list2 = [100, 34, 75, 3, 56, 33, 23, 86]
# 
# list3 = list1 + list2
# print("List3(unsorted):", list3)
# 
# count = len(list3)
# 
# list4 = []
# i = 0
# while count != 0:
#     a = min(list3)
#     list4.insert(i, a)
#     b = list3.index(a)
#     list3.pop(b)
#     count -= 1
#     i += 1
#     
# print("List4:          ", list4)
# 
# print()
#-------------------------------------------------------------------------------
#*******************************************************************************
# sort without using built in functions

# the plan:
# take the first value into a variable --> A
# compare the next value with A, if higher, check next value 
#                             , if lower,  replace A with this value, continue checking following values
# do as before looped
# when loop ends and all values have been compared with A, this means that A is the lowest value
# place this A into the new-list[0] 
# delete A from the original list
# count number should subtract 1
# the A will take the first value again and compare it with the next value as done before
# this cycle continues until the original loop has only one item left 
# this last item will go in the new-list[original count - 1] 
 
# the loop needs to check each item it runs if the count is more than 1 or not 
# if not then last item needs to go to its right place in new-list

# inner loop cycles once around all values in original list until it finds A and places A into new-list 
# x++ each time until lowest value is found

# outer loop starts with x = 0
# outer loop resets x back to 0 after inner loop exit ends...so the original list index does not go out of range

# after outer loops ends print new-list

list1 = [100, 24, 23, 76, 56, 22, 10, 96]
list2 = [100, 34, 75, 3, 56, 33, 23, 86]
list3 = list1 + list2

print("List1: ", list1)
print("List2: ", list2)
print("List3: ", list3)

count = len(list3)
list4 = [] 
i = 0
m = 0

while(count != 0):
    x = 0
    n = x + 1
    if count > 1:
        a = list3[m]
        b = list3[x+1]
        for x in range(count):
            if a <= b:
                x = x + 1
            else:
                m = n
                #a = b                
        
        list4.insert(i,a)
        del a
        i += i
        count -= 1
        m += 1 
    else:
        a = list3[x]
        count = 0

print()  
print("List4: ", list4)


print("        Sorted List3 to cross-check above")
list3.sort()
print("       ",list3)















# while(count != 0):
# #for x in range(count):
#     if list3[x] < list3[x+1]:
#         
#         
#         
#         #list4.insert(x,list3[x])
#         #del list3[x]
#         x += 1
#         count -= 1
#          
# #    if count == 1:
# #        list4.insert(count-1, list3[x])
#          

