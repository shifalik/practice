'''
Created on Feb 6, 2018

@author: shifa
'''

#Palindrome String
#example: wow


class Palindrome:
    "Finds out if the inputed string is a palindrome or not"
    
    #def __init__(self):
    #    self.str1 = str1

    def secretformula(self):
        arr1 = list(str(str1))
        count = len(arr1)
        x = 0
        for x in range(count):
            if arr1[x] == arr1[count-(x+1)]:
                x += 1
            else:
                print("This is not a palindrome.")
                break

        if count == x:
            print("This is a palindrome.")    

   
str1 = input("Enter your string: ")
a = Palindrome()    
a.secretformula()



    








#PALINDROME STRING!!
# 
# str1 = input("Enter your string: ")
# 
# arr1 = list(str(str1))
# count = len(arr1)
# x = 0
# 
# for x in range(count):
#     if arr1[x] == arr1[count-(x+1)]:
#         x += 1
#     else:
#         print("This is not a palindrome.")
#         break
# 
# if count == x:
#     print("This is a palindrome.")    



