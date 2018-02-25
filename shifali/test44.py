'''
Created on Feb 8, 2018

@author: shifa
'''
#from test.test_buffer import indices

# Strings continued

# lower() returns a copy of the string in which all 
# case-based characters have been lower-cased
print('lower()')

str1 = "THIS IS STRING EXAMPLE...WOW!!!"
print(str1.lower())

print()
#---------------------------------------------------
# lstrip() returns a copy of the string in which all chars 
# have been stripped from the beginning of the string
# default is the whitespace char

# str.lstrip([chars])
# chars - can give what chars have to be trimmed
print("lstrip()")

str2 = "              this is string example...wow!!!"
print(str2.lstrip())  # also works with " "

str3 = "********this is string example...wow!!!*****"
print(str3.lstrip('*'))

# strips from the beginning ONLY
print()
#----------------------------------------------------
# maketrans() returns a translation table that maps each
# character in the intabstring into the character at the 
# same position in the outtab string
# this table is passed to the translate() function

# intab and outtab must be same length
# str.maketrans(intab.outtab)

# intab is string having actual characters
# outtab is the string having corresponding mapping char

print("maketrans()...table to be used with translate()")

intab = "aeiou"
outtab = "12345"

str4 = "this is string example...wow!!!"
print(str4)

trantab = str4.maketrans(intab, outtab)
print(str4.translate(trantab))

# each vowel in string is replaced by its vowel position

print()
#-------------------------------------------------------
# max() returns the max alphabetical char from the string
# max(str)

print('max(str)')

str5 = "this is string example....really!!!" 
print("Max character:" + max(str5))
# if z, then it will be highest

str6 = "this is string example...wow!!!"
print("Max character:" + max(str6))
# if abc...then c is max

print()
#-------------------------------------------------------
# min() returns the min alphabetical char from the string
# min(str)

print("min(str)")

str7 = "www.tutorialspoint.com"
print("Min character: " + min(str7))

str8 = "TUTORIALSPOINT"
print("Min character: " + min(str8))

# decimal comes first as lowest
# A is before a

print()
#------------------------------------------------------
# replace() returns a copy of the string in which the 
# occurrences of old have been replaced with new optionally
# restricting the number of replacements to max

# str.replace(old, new[,max])
# old - old substring to be replaced
# new - new substring that replaces
# max - optional argument, only first count occurrences are
# replaced

print('replace(old, new[,max])')

str9 = "this is string example...wow!!! this is really string"
print(str9.replace("is", "was"))

print(str9.replace("is", "was", 3)) 
# only replaces 3 times

print()
#------------------------------------------------------
# rfind() returns the last index where the substring str is
# found, or -1 if no such index exists, optionally
# restricting the seardch to string[beg:end]

# SAME AS FIND() BUT SEARCH BACKWARDS IN STRING

# str.rfind(str, beg = 0 end = len(string))
# str - specifies the string to be searched
# beg - starting index (default is 0)
# end & minus - this is the ending index, default is 
# equal to the end of the string

# returns last index if found, otherwise -1
print('rfind()')

str10 = "this is really a string example...wow!!!"
str11 = "is"

print(str10.rfind(str11))
print(str10.rfind(str11, 0 , 10))
print(str10.rfind(str11, 10 , 0))

print()
# ___ ____ _____ ______ _______ _______
print('find()')

print(str10.find(str11))
print(str10.find(str11, 0, 10))
print(str10.find(str11, 10, 0))

print()
#---------------------------------------------------
# rindex() returns the last index where the substring str
# is found or raises an exception if no such index exists,
# optionally restricting the search to string[beg:end]

# SAME AS INDEX() BUT SEARCH BACKWARDS IN STRING

# str.rindex(str, beg = 0 end = len(string))

print('rindex()')

# returns last index if found otherwise exception 
# if str not found

str12 = "this is really a string example...wow!!!"
str13 = "is"

print(str12.rindex(str13))
# print(str12.rindex(str13, 10))
# prints exception as it is supposed to do

print()
#----------------------------------------------------
# rjust() returns the string right justified in a 
# string of length width

# padding is done using the specified fillchar
# (default is a space)
# the original string is returned if width is less than
# len(s)

# str.rjust(width[,fillchar])
# width is the string length in total after padding
# fillchar is filler char, default is space

print("rjust()")

str14 = "this is string example.....wow!!!"
print("Right Justified", str14.rjust(50, '*'))

print("Left Justified", str14.ljust(50, '*'))
# ljust() puts padding on right side
# rjust puts padding on left side

print()
#----------------------------------------------------
# rstrip() returns a copy of the string in which all chars
# have been stripped from the end of the string
# default is whitespace char

# str.rstip([chars])
# can choose chars

print('rstrip()')

str15 = "     this is string example...wow!!"
print(str15.rstrip())

str16 = "*****this is string example...wow!!"
print(str16.rstrip('*'))

print()
#-----------------------------------------------------
# split() returns a list of all the words in the string
# using str as the separator 
# splits on all whitespace if left unspecified 
# optionally limiting the number of splits to num

# str.split(str = "", num = string.count(str))
# str - any delimeter by default it is spacce
# num is the number of lines to be made

print('split()')

str17 = "this is string example....wow!!!"
print(str17.split())
print(str17.split('i', 1))  # 1 is number of lines to be made
print(str17.split('w'))

print()
#-------------------------------------------------------
# splitlines() returns a list with all the lines in string
# optionally including the line breaks 
# (if num is supplied and is true)

# str.splitlines(num = string.count('\n')

# returns true if found matching string otherwise false

print('splitlines()')

str18 = "this is \nstring example....\nwow!!!"
print(str18.splitlines())

# splits strings at all (or num) newlines and returns 
# a list of each line with newlines removed

print()
#-------------------------------------------------------
# startswith() checks whether the string starts with str,
# optionally restricting the matching with the given indices
# start and end

# str.startswith(str, beg = 0, end = len(string))
# str - string to be checked
# beg - optional parameter to set start index of matching
# boundary
# end - optional parametere to set start index of the 
# matching boundary

print('startswith()')

str19 = "this is string example...wow!!!"
print(str19.startswith('this'))
print(str19.startswith('string', 8))  # start from 8 search
print(str19.startswith('this', 2, 4))  # from 2-4 

print()
#-------------------------------------------------------
# strip() returns a copy of the string in which all chars 
# have been stripped from the beginning and the end of the
# string (default whitespace chars)

# str.strip([chars])
# chars to be removed from beginning or end of string

print('strip()')

str20 = "*******this is string example....wow!!!******"
print(str20.strip('*'))

print()
#-------------------------------------------------------
# swapcase() returns a copy of the string in which all the 
# case-based characters have had their case swapped

# str.swapcase()

print('swapcase()')

str21 = "this is string example...wow!!!"
print(str21.swapcase())

str22 = "This Is String Example...WOW!!!"
print(str22.swapcase())

# makes lower case ----> upper cased
# makes upper case ----> lower cased

print()
#--------------------------------------------------------
# title() returns a copy of the string in which 
# first characters of all the words are capitalized

# str.title()

print('title()')

str23 = "this is string example....wow!!!"
print(str23.title())

print()
#--------------------------------------------------------
# translate() returns a copy of the string in which all 
# characters have been translated using table 
# constructed with the maketrans() function
# optionally deleting all charaters found in the string 
# deletechars

# str.translate(table[,deletechars])
# table - use the maketrans() helper function to create
# a translation table

# look at str4 for ref

print('translate()')

# from string import maketrans 
# required to call maketrans function

intab = "aeiou"
outtab = "12345"
str24 = "this is string example....wow!!!"

trantab = str24.maketrans(intab, outtab)

print(str24.translate(trantab))

print('delete used:')

deltab = "xm"  # added line

trantab = str24.maketrans(intab, outtab, deltab)
print(str24.translate(trantab))

print()
#------------------------------------------------
# upper() returns a copy of the string in which all
# case-based characters have been uppercased

# str.upper()

print('upper()')

str25 = "this is string example....wow!!!"
print(str25.upper())

print()
#-------------------------------------------------
# zfill() pads string on left with zeros to fill width

# str.zfill(width)
# width- final width of the string 

print('zfill()')

# here is the padded string output
# FILLS THE REMAINING SPACES IN WIDTH WITH PADDING

str26 = "this is string example....wow!!!"
print(str26.zfill(40))
print(str26.zfill(50))

print()
#-------------------------------------------------
# isdecimal() checks whether the string consists of only
# decimal characters. 

# str.isdecimal()

print('isdecimal()')

# returns true if characters are decimal otherwise false

str27 = "this2017"
print(str27.isdecimal())

str28 = "23443434"
print(str28.isdecimal())

print()
#-------------------------------------------------


