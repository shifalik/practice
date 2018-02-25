'''
Created on Feb 22, 2018

@author: shifa
'''

#FILES I/O

#----------------------------------------------------------
#printing to screen
print("Python is a really great languge", "isn't it?")

print()
#----------------------------------------------------------
#Reading Keyboard Input

#input() 
#reads data from keyboard as a string

print("Say something:")
a = input()
print(a)

print()
#----------------------------------------------------------
#the input function

#input([prompt]) function assumes that the input is a vaild 
#python expression and returns the evaluated result to you

x = input("something:")
print(x)

x = input("something:")
print(x)

print()
#----------------------------------------------------------
#OPEN function

#open() is python's built-in function
#this function creates a file object

#SYNTAX
# file object = open(file_name [, access_mode][, buffering])

#file_name --> name of your file

#access_mode --> determines the mode the file has to be 
#opened in(read/write/append/etc)
#it is a optional parameter and the default file access 
#mode is read (r)

#buffering --> if value is 0 then no buffering 
#              if value is 1 then line buffering is performed
#                    while accessing a file
#              if value is x>1 then buffering action is  
#                    performed with the indicated buffer size
#              if value is negative, the buffer size is the 
#                    system default

#r (is default) opens a file to read only
#rb opens in binary format
#r+ opens files for reading and writing
#rb+ opens files read/write in binary
#w opens a file to write only/overwrites/creates new 
#w+ opens file for writing and reading/overwrites/creates new
#wb+ does above in binary
#a opens file for appending/creates new file for writing
#ab opens file for appending in binary/creates for writing
#a+ opens a file for appending/reading or creates for read/write
#ab+ appending/reading in binary or creates for read/write

#----------------------------------------------------------
#file object attributes

#once a file is opened, you have on file object

#file.closed
#returns true if file is closed

#file.mode
#returns access mode with which file was opened

#file.name
#returns name of the file

fo = open("foo.txt", "wb")
print("name of file:", fo.name)
print("closed or not:", fo.closed)
print("opening mode:", fo.mode)
fo.close()

print()

#self
hi = open("test1.py", "r")
print("name of file:", hi.name)
hi.close()


print()
#--------------------------------------------------------
#the close() method
#flushes any unwritten info and closes the file object
#python automatically closes a file when the ref object 
#of a file is reassigned to another file

#SYNTAX
#fileObject.close()

fo = open("foo.txt", "wb")
print("Name of file: ", fo.name)
fo.close()

print()
#--------------------------------------------------------
#Reading and Writing Files

#the write() method writes any string to an open file

#SYNTAX
#fileObject.write(string)

fo = open("foo.txt", "w")
fo.write("Python is a great language. \nYeah its great!!\n")
fo.close()

#if i open file foo.txt
#yes it says it there

#--------------------------------------------------------
#read() method
#reads a string from an open file

#SYNTAX
#fileObject.read([count])

#the passed parameter is the number of bytes to be read
#from the opened file

fo = open("foo.txt", "r+")
str1 = fo.read(10)
print("Read String is:", str1)

fo.close()

#if the count is missing, then it tries to read as much 
#as possible, maybe until the end of the file

print()
#---------------------------------------------------------
#File Positions
#tell() method tells you the current position within the
#file or the next read/write position

#seek(offset[,from]) method changes the file position
#offset tells the number of bytes to be moved
#from tells the reference position from where the bytes 
#are to be moved

#from = 0, start from beginning of file

fo = open("foo.txt", "rt")
str1 = fo.read(10)
print("Read string is:", str1)

position = fo.tell()
print("Current file position:", position)

position = fo.seek(0,0)
str1 = fo.read(10)
print("Again read string is:", str1)

fo.close()

print()
#---------------------------------------------------------
#Renaming and Deleting Files

#os is a built in module that provides methods to help
#to perform file-processing operations

#need to import os first

#rename() method 
#takes two arguments
#current file name and new filename

#SYNTAX
#os.rename(current_file_name, new_file_name)

#import os
#os.rename("test1.txt", "test2.txt")


#---------------------
#below self
# test = open("test1.txt", "w")
# print("Name of file:", test.name)
# test.close()

#os.rename("test1.txt", "test2.txt")

#self no work
#test1 = open("test2.txt", "w")
#print("Name of file:", test1.name)
#test1.close()

print()
#--------------------------------------------------------
#remove() method
#to delete files by supplying the name of the file
#to be deleted as the argument

#SYNTAX
#os.remove(file_name)

#import os
#os.remove("text2.txt")

print()
#--------------------------------------------------------
#Directories 
#uses the os module to CREATE/REMOVE/CHANGE DIRECTORIES

#-------------------------------------------
#mkdir() method
#creates directories in the current directory

#SYNTAX
#os.mkdir("newdir")

#import os
#os.mkdir("test")

#-------------------------------------------
#chdir() method
#change the current directory

#the argument is the name of the new 
#current directory that you want

#SYNTAX
#os.chdir("newdir")

#import os
#os.chdir("/home/newdir")

#--------------------------------------------
#getcwd() method
#displays the current working directory

#SYNTAX
#os.getcwd()

import os
a = os.getcwd()     

print("Location of current working directory:")
print(a)
#gives location of current directory

#---------------------------------------------
#rmdir() method
#deletes the directory 

#before removing, all contents should be removed

#SYNTAX
#os.rmdir('dirname')

#import os
#os.rmdir("/temp/test")

#it is required to give fully qualified name 
#of the directory 
#otherwise it would search for that directory 
#in the current directory
#----------------------------------------------
#FILE AND DIRECTORY RELATED METHODS

#there are other file object methods and 
#OS object methods 

#long list to manipulate/process files and directories













