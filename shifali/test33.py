'''
Created on Jan 26, 2018

@author: shifa
'''

#continue statement 
#returns the control to the beginning of the current loop

#loop starts the next iteration without executing 
#the reaming statements in the current iteration

for letter in "Python":
    if letter =="h":
        continue
    print("Current Letter:", letter)
#'h' is skipped over
#-------------------------------------
print()
#skips line

var = 10
while var > 0:
    var = var -1
    if var == 5:
        continue
    print("Current Variable value:", var)
#doesn't print the value 5

print("End of program")

