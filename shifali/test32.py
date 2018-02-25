'''
Created on Jan 25, 2018

@author: shifa
'''

#break example 2

a = 1
numbers = [11,33,55,39,55,75,37,21,23,41,13]

#i placed while here
while(a == 1):
    no = int(input("Any number:"))
    
    for num in numbers:
        if num == no:
            print("Number found in list")
            break
    else:
        print("Number not found in list")

#my below addition
    ch = str(input("Want to exit:"))
    if (ch == "yes"): 
        print("Program has terminated")
        break

    








