'''
Created on Jan 22, 2018

@author: shifa
'''
# elif
# allows you to check multiple expressions
# for True and execute a block a code as 
# soon as one of the conditions evaluates
# to True

# there can be an arbitrary number of 
# elif statements following an if

# there are no switch or cases statements

amount = int(input("Enter amount: "))

if amount < 1000:
    discount = amount * 0.05
    print("Discount", discount)
elif amount < 5000:
    discount = amount * 0.10
    print("Discount", discount)
# i added below elif     
elif amount < 10000:
    discount = amount * 0.25
    print("Discount", discount)
# back to program
else:
    discount = amount * 0.15
    print("Discount", discount)
    
print("Net payable:", amount - discount)

#-----------------------------------------
# example 2
# num = int(input("enter number"))
# 
# if num > 0:
#     if num > 5:
#         print ("Big Number")
#     elif num < 5:
#         print ("Small Number")
# else:
#     print("Negative Number")

