'''
Created on Jan 25, 2018

@author: shifa
'''

#break statement
#premature termination of current loop

for letter in "Python":
    if letter == "h":
        break
    print("Current Letter:", letter)
    
#-------------------------------------

var = 10
while var > 0:
    print("Current variable value:", var)
    var = var -1
    if var == 5:
        break
    
print("End of program")
    
    
    
    
    
    
    

   

