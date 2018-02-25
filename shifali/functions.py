'''
Created on Feb 16, 2018

@author: shifa
'''
# Function is a block a organized and reusable code
# that is used to perform a single action
# python has built in functions like print()
# can make user defined functions
from functools import total_ordering

# Defining a function
# must begin with def followed by function name and
# parentheses (())
# parameter/arguments should be inside ()
# first statement can be a documentation string
# starts with : and indented
# return [expression] exits a function
# no return statement = return None

# FORMAT
# def functionname(parameters):
#     "function_docstring"
#     function_suite
#     return[expression]

# parameters need to be defined in same order as mentioned


#----------------------------------------------------------
# Function Definition
# Takes string into input parameter and prints it
def printme(str1):
    "This prints a passed string into this function"
    print (str1)
    return


# Calling Function    
printme("This is first call to the user defined function!")
printme("Again second call to the same function")

print()
#----------------------------------------------------------
# Pass by Reference vs. Value


# Function Definition
def changeme(mylist):
    "This changes a passed list into this function"
    print("Values inside the function before change: ", mylist)
    mylist[2] = 50
    print("Values inside the function after change: ", mylist)
    return


# Calling Function
mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function: ", mylist)

# Mainting ref to passed obj and appending values in same obj

print()
#----------------------------------------------------------
# argument is being passed by ref and the ref is being
# overwritten inside the called function


# Function Definition
def changeme1(mylist1):
    "This changes a passed list into this function"
    mylist1 = [1, 2, 3, 4]
    print("Values inside the function: ", mylist1)
    return


# Calling Function
mylist1 = [10, 20, 30]
changeme1(mylist1)
print("Values outside the function: ", mylist1)

# mylist1 is local to the function changeme1 

print()
#-----------------------------------------------------------
# Function Arguments
# REQUIRED Arguments are those that are passed to a function
# in correct positional order

# number of arguments in the function call should match 
# exactly with the function definition

# reference to printme function earlier

# def printme(str1):
#     "This prints a passed string into this function"
#     print (str1)
#     return

# printme() 
# will generate error if nothing is placed inside ()

#----------------------------------------------------------
# Keyword Arguments
# related to function calls, caller ids the arguments by
# parameter name

printme(str1="My string")  # uses keyword str1
# python can use keywords to match the values with parameters
# allows to skip arguments and/or place them out of order

print()


# proper example
def printinfo(name, age):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age: ", age)
    return


printinfo(age=50, name="miki")

print()
#---------------------------------------------------------
# Default Arguments
# argument that assumes a default value if a value is not 
# provided in the function call for that argument


def printinfo1(name1, age1=35):
    "This prints a passed info into this function"
    print("Name: ", name1)
    print("Age: ", age1)

    
printinfo1(age1=50, name1="miki")
printinfo1(name1="miki")

print()
#---------------------------------------------------------
# Variable-length Arguments
# may need more arguments than you specified while 
# defining the function

# FORMAT FOR NON_KEYWORD VARIABLE ARGUMENTS 
# def functionname([formal_args,] *var_args_tupe):
#     "function_docstring"
#     function_suite
#     return [expression]

# (*) is placed before the variable name that holds the 
# values of all non-keyword variable arguments

#tuple remains empty if no additional arguments are 
#specified during function call

def printinfo2(arg1, *vartuple):
    "This prints a variable passed arguments"
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return

#calling
printinfo2(10)
printinfo2(70,60,50)

print()
#---------------------------------------------------------
#The Anonymous Functions

#functions not declared in standard manner by using def
#can use the lambda keyword to create small anonymous func

#lambda
#takes any number of arguments
#returns only one value in form of expression
#can not contain commands/multiple expressions
#cannot be a direct call to print, it needs expression
#have their own local namespace
#cannot access variables other than those in their 
#parameter list and those in the global namespace

#FORMAT
#lambda [arg1 [,arg2, ..... argn]]: expression

#function definition
sum1 = lambda arg1, arg2: arg1 + arg2

#call sum1 as function
print("Value of total: ", sum1(10,20))
print("Value of total: ", sum1(20,20))

print()
#---------------------------------------------------------
#the return statement

#return [expression] exits a function
#optionally passing back an expression to the caller
#if no arguments then considered return None

#fun def
def sum2(arg1, arg2):
    total = arg1 + arg2
    print("Inside the function:", total)
    return total

#call
total = sum2(10,20)
print("Outside the function:", total)

print()
#----------------------------------------------------------
#Scope of variables
#depending on where the variable is declared, 
#depends its accessibility

#two basic scopes of variable: GLOBAL and LOCAL
#variables defined inside a function body have LOCAL scope
#variables defined outside have a GLOBAL scope

#local variables can be accessed only inside the function
#global variables can be accessed throughout the program
#body by all functions

total = 0 #global

def sum3(arg1,arg2):
    total = arg1 + arg2 #local
    print("Inside the function local total:", total)
    return total 

sum3(10,20)
print("Outside the function global total:", total)

print()
#--------------------------------------------------------



















