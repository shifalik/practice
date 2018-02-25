'''
Created on Jan 24, 2018

@author: shifa
'''
#using else statements with for loops
#else is executed only if for loops 
#terminates normally 
#(not by break statement)

numbers = [11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
    if num % 2 == 0:
        print('the list contains an even number')
        break
else:
    print('the list does not contain an even number')

#this is a program for searching for an 
#even number in this given list






