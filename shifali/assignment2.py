'''
Created on Feb 2, 2018

@author: shifa
'''

#QUESTION: Reverse String

#The Plan
#-------------------------------
#get input
#count amount of characters used

#need to store characters in array
#print array backwards
#-------------------------------

value = input("Enter your string: ")
print()

total = 0
for char in value:
    print("Reading Character:", char)
    total = total + 1 
    
print("Total number of characters used:", total)
 
print()
#a = list(str(value))                            #looked up
a = list(value)
print("Placing your string into an array:")
print(a)

print()
print("Now Printing Array Backwards:")
n = 1
i = 0
b = []

for obj in a:
    print("Posting Character:", a[total-n])
    b.insert(i, a[total-n])                     #looked up
    n = n+1
    i = i+1

print()
string1 = ''.join(b)                            #looked up
print("The Reverse String is:", string1)
print("END OF PROGRAM")

#NOTES
#________________________________________________________
#print(sizeof(a))

# print("Now Printing Backwards")
# for obj in a:
#     print("Posting Character:", obj)
#     total = total - 1

#print(a[0:3])
#can print selected
#cant do 3:0

#idea
#possibly can be 0:total

#print("\nPrinting characters:", a[0:total])

#can use for loop here possibly

#print(a[total-n])
# m = 0
# while(total == m):
#     print(a[total-m])
#     m = m + 1


