'''
Created on Feb 7, 2018

@author: shifa
'''

# Unicode String
# Built-in String Methods to manipulate strings

#-----------------------------------------------
# capitalize

str1 = "this is string example....wow!!!"
print("str1.capitalize():", str1.capitalize())

print()
#-----------------------------------------------
# center()

# str.center(width[, fillchar])
# width is total width of string
# fillchar is the filler character

str2 = "this is string example...wow!!!"
print("str2.center(40,'a'):", str2.center(40, 'a'))

print()
#-----------------------------------------------
# count() returns the number of occurrences of substring
# sub in the range[start,end]

# str.count(sub, start = 0, end = len(string))

# sub is the substring to be searched
# start-- search starts from this index default is 0
# end is ends from this index default is last index

str3 = "this is string example....wow!!!"
sub = 'i'
print("str3.count('i'):", str3.count(sub))

sub = 'exam'
print("str3.count('exam,10,40):", str3.count(sub, 10, 40))
#40 = 40 - 1 = 39 will be used
#string.count(sub, n, n - 1)

print()
#-----------------------------------------------
# decode() decodes the string using the 
# codec registered for encoding
# str.decode(encoding = 'UTF-8', errors = 'strict')

# encoding -has possible schemes
# errors -there are other options avail for error handling
# import base64
# str4 = "this is string example...wow!!!"
# str4 = str4.encode('base64','strict');
# print("Encoded String:" + str4)
# print("Decoded String:" + str4.decode('base64','strict'))

# print() 
#------------------------------------------------
# encode() returns an encoded version of the string
# str.encode(encoding = 'UTF-8', errors = 'strict')

import base64
 
str5 = "this is string example...wow!!!"
str5 = base64.b64encode(str5.encode('utf-8', errors='strict'))
print("Encoded string:", str5)

print()
#-------------------------------------------------
# string endswith()
# returns true if the string ends with the specified suffix
# otherwise returns false

# str.endswith(suffix[,start[,end]])

# start/end --slicing positions
# suffix can be string or tuple of suffixes to look for
print("endswith()")

str6 = 'this is string example...wow!!!'
suffix = '!!'
print(str6.endswith(suffix))
print(str6.endswith(suffix, 20))

suffix1 = 'exam'
print(str6.endswith(suffix1))
print(str6.endswith(suffix1, 0, 19))

print()
#----------------------------------------------------
# expandtabs() returns a copy of the string in which 
# the tab characters '\t' are expanding using spaces
# default 8 tabsize

# str.expandtabs(tabsize = 8)
# tabsize specifies the number of characters to be replaced 
# for a tab character '\t'
print("expandtabs()")

str7 = "this is\tstring example....wow!!!"

print("Original String:      " + str7)
print("Default expanded tab: " + str7.expandtabs())
print("Double expanded tab:  " + str7.expandtabs(16))

print()
#----------------------------------------------------
# find()
# str.find(str, beg = 0 end = len(string))
# str is the string to be searched
# beg is the starting index by default it is 0
# end is the ending index by default its equal to the
# length of the string
print("find()")

str8 = "this is string example...wow!!!"
str9 = "exam"

print(str8.find(str9))
print(str8.find(str9, 10))
print(str8.find(str9, 40))

# returns index found otherwise -1
print()
#-----------------------------------------------------
# index() method determines if the string str occurs in string 
# or in a substring of strin
# similar to find() but raises exception if sub is not found

# str.index(str, beg = 0 end = len(String))

print("index()")

str10 = "this is string example....wow!!!"
str11 = "exam"

print(str10.index(str11))
print(str10.index(str11, 10))
# print(str10.index(str11, 40))
# prints error b/c substring not found
# yes supposed to throw exception

print()
#---------------------------------------------------
# isalnum() check whether the string consists of 
# alphanumeric characters
print("isalnum()")

str12 = "this2017"  # has to be no space!
print(str12.isalnum())

str13 = "this is string example....wow!!!"
print(str13.isalnum())

# true if all characters in string are alphanumeric and
# there is at least one character otherwise false

print()
#---------------------------------------------------
# isalpha() checks whether the string consists of 
# alphabetic characters only
print("isalpha()")

str14 = "this"  # no space and digit in this string!
print(str14.isalpha())

str15 = "this is string example...wow!!!"
print(str15.isalpha())

# true is all characters in the string are alphabetic 
# and there is at least one character, false otherwise

print()
#----------------------------------------------------
# isdigit() checks whether the string consists of
# digits only

print("isdigit()")

str16 = "123456"  # only digits, there can be no spaces
print(str16.isdigit())

#works on whole number only no decimal spaces

str17 = "this is string example...wow!!!"
print(str17.isdigit())

# true if all characters in the string are digits 
# and there is at least one character, false otherwise

print()
#-------------------------------------------------------
# islower() checks whether all the case-based characters
# letters of the string are lowercase

print("islower()")

str18 = "THIS is string example...wow!!!"
print(str18.islower())

str19 = "this is string example...wow!!!"
print(str19.islower())

# true if all cased characters in the string are lowercase
# and there is at least one cased character, otherwise false

print()
#--------------------------------------------------------
# isnumeric() checks whether the string consists of only
# numeric characters
# method is present only on unicode objects

print("isnumeric()")

str20 = "this2017"
print(str20.isnumeric())

str21 = "23443434"  # false if space used 
print(str21.isnumeric())

# true is all characters in the string are numeric
print()
#--------------------------------------------------------
# isspace() checks if string consists of whitespace

print("isspace()")

str22 = "      "  # has to be completely empty
print(str22.isspace())

str23 = "This is string example....wow!!!"
print(str23.isspace())

# true if there are ONLY whitespace characters in the string
# and there is at lease one character, false otherwise

print()
#-------------------------------------------------------
# istitle() checks whether all the case-based characters
# in the string following non-casebased letters are 
# uppercase and all other case-based characters are 
# lowercase

print("istitle()")

str24 = "This Is String Example...Wow!!!"
print(str24.istitle())

str25 = "This is string example...wow!!!"  # hellO doesnt work
print(str25.istitle())

# true is the string is titlecased and there is at least
# one character 

print()
#------------------------------------------------------
# isupper() checks whether all the case-based characters
# letters of the string are uppercase

print("isupper()")

str26 = "THIS IS STRING EXAMPLE...WOW!!!"
print(str26.isupper())

str27 = "THIS is string example...wow!!!"  # works with A only
print(str27.isupper())

# true is all cased characters in the string are uppercase
# and there is at least one cased character, false other

print()
#------------------------------------------------------
# join() returns a string in which the string elements of
# sequence have been joined by str separator

print("join()")

s = "-"  # how you want them to interact works with blank also
seq = ("a", "b", "c")  # this is a seq of strings
print(s.join(seq))

# returns a string concatenation 
print()
#-------------------------------------------------------
# len() returns the length of the string

print("len()")

str28 = "this is string example....wow!!!"
print("Length of the string:", len(str28))

print()
#------------------------------------------------------
# ljust() returns the string left justified in a string
# of length width; padding is done using filchar
# default is a space
# original string is returned if width is less than len(s)

# str.ljust(width[,fillchar])
# width is string length in total after padding
# fillchar is filler character, default is a space

print("ljust()")

str29 = "this is string example....wow!!!"
print(str29.ljust(50, '*'))

print()
#------------------------------------------------------

