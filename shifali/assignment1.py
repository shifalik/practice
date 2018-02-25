'''
Created on Feb 1, 2018

@author: shifa
'''

#Question: REVERSE INTEGER

#The Plan
#-------------------------------
#get input
#count amount of numbers used

#need to store number in array
#print array backwards
#-------------------------------

#need to find a way to ensure only integers 
#numerical are accepted

value = int(input("Enter your number:"))
print()

a = list(map(int, str(value)))                  #looked up
print("Your number as a array: ", a)
print()

total = 0
n = 0
for num in a:
    print("Reading Number:", a[n])
    n = n + 1
    total = total + 1
print("Total number of values used:", total)
print()

print("Now printing number backwards:")

z = 1
rev = []
i = 0
for digit in a:
    print("Posting Number:", a[total-z])
    rev.insert(i, a[total-z])
    z = z + 1
    i = i + 1
print()

print("The Reverse Array is:", rev)

str1 = ''.join(str(e) for e in rev)         #looked up
print("The Reverse Number is:", str1)
    
