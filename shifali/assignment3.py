'''
Created on Feb 3, 2018

@author: shifa
'''

# palindrome number is a number that remains the same when its digits are reversed 
# it is symmetrical
# ex 121.....1221....etc
# ex 0-9...11,22,.....etc

# compare first number with last number 
# keep comparing until reach middle 

# cases to consider:
# single cases 0 1 2 3 4 5 6 7 9 are palindromes by themselves
# double cases 11 22 33 ......99 are palindromes
# triple cases 121 272 etc
# quad cases 1221 4554
# ...so on

# THE PLAN
# ___________________
# get user input
# check to see if it's length is 1 ----if so then it is an palindrome

# if length is 2 -------->  put into array and 
# compare array[0] with array [1] check to see if ==
# if == then they are palindrome otherwise they are not

# if length is 3 -----> 
# put into array and compare array[0] with array[2] (last value of array)--> can name this total
# need two variables a and b 
# one for array[beginning] --> array[a]
# one for array[end] ---> array[b]
# the one for the beginning needs to add each time ---> a + 1
# one for the end needs to subtract each time ---> b - 1
#------------------------------------------------------------------------>
#                                    if its even then it will be enough to compare all values, can tell if it is palindrome or not

# if array[a] = array[b] meaning that both values of a and b are the same 
# then check if the value inside is the same if so, then its an palindrome

# if at any point the compares fail then break because its not a palindrome
# ______________________________________________________________________________________

print("Welcome to the Palindrome Testing Center.")
print()
test = int(input("Please enter your number: "))

# put test into array
box = list(str(test))
print("Placing your number in an array:", box)

box1 = []
while(test!=0):
    lastDigit = test % 10
    box1.append(lastDigit)
    test = test //10
box1.reverse()
print("Placing your number in an array by deepak:", box1)

big = len(str(test))  # looked up
print("The length of your number is:" , big)
print()
print("VERDICT:")

total = 0
for i in range(big):
    if box[i] == box[big-(i+1)]:
        total += 1
    else:
        print("Sorry, this is not a palindrome!")
        break

if total == big:
    print("This is a palindrome!")





#ONE case:
# if big == 1:
#     print("Result: This is a palidrome!")
    
#TWO case:
# box[n] 
# box[big - m]
# 
# if box[n] == box[big-m]:
#     print("This is a palidrome!")
# else:
#     print("Sorry, this is not a palidrome!")