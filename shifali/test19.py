'''
Created on Jan 22, 2018

@author: shifa
'''
#if else statements
#there can be at most only one else 

amount = int(input("Enter amount: "))
#int=integer
#data type declaration 

if amount < 1000:
    discount = amount * 0.05
    print("Discount", discount)
else:
    discount = amount * 0.10
    print("Discount", discount)
    
print("Net payable:", amount-discount)
#amount-discount is subtraction

