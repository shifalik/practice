'''
Created on Feb 21, 2018

@author: shifa
'''

# Modules
# allow you to organize code
# group related code into a module makes code easier to use/understand
# it is a python object with arbitrarily named 
# attributes that you can bind and reference
#           ----------
# its a file with python code
# modules can define functions/classes/variables 
# or have runnable code

# can use any file as a module by executing an import 
# statement in some other python source file

# >>>>>>>>>>>>>>>
# import SYNTAX
# import module1[, module2[,...moduleN]]

# when import, it imports the module if the module is 
# present in the search path

# search path is a list of directories that the interpreter
# searches before importing a module

import support  # uses support.py here as reference

support.print_func("Zara")

# module is loaded once regardless of the number of times
# it is imported
# it prevents the module execution from happening repeatedly
# if multiple imports occur

print()
#---------------------------------------------------------
# the from...import statement

# from statement lets you import specific attributes from
# a module into the current namespace

# from...import SYNTAX
# from modname import name1[, name2[, ... nameN]]

from fib import fib
a = fib(100)
print(a)

# the statement doesn't import the entire module fib into 
# the current namespace 
# it just introduces the item fibonacci from the module
# fib into the global symbol table o the importing module

print()
#---------------------------------------------------------
# the from...import* statement

# it is possible to import all the names from a module
# into the current namespace by using the following 
# import statement

# from modname import*

#---------------------------------------------------------
# executing modules as scripts

# within a module, the module's name (as a string) is 
# available as the value of the global variable __name__

# the code in the module will be executed just as if it were
# imported but with the __name__ set to "__main__"

# see fib file
#---------------------------------------------------------
# Locating Modules

# when importing a module it searches here:
# the current directory
# if not found then checks each directory in the shell 
# variable PYTHONPATH
# if all fails, checks default path 

# the module search path is stored in the system module sys
# as the sys.path variable

# this variable contains the current directory, PYTHONPATH
# and the installation-dependent default
#---------------------------------------------------------
# The PYTHONPATH Variable

# PYTHONPATH is an environment variable
# contains a list of directories

# its syntax is same as shell variable PATH

# Example:
# set PYTHONPATH = c:\pthon34\lib
#---------------------------------------------------------
# Namespaces and Scoping

# variables are names (identifiers) that map to objects

# namespace is a dictionary of variable names (keys) and
# their corresponding objects (values)

# python can access variables in a local namespace and
# in the global namespace 

# if a local and global variable have the same name,
# the local variable shadows the global variable

# each function has its own local namespace
# class methods follow the same scoping rule as ordinary func

# python makes educated guesses global/local variable
# it assumes that any variable assigned a value
# in a function is local

# in order to assign a value to a global variable within
# a function, you have to use a global statement

# statement global VarName 
# this tells python that varname is a global variable
# python stops searching the local namespace for the variable

Money = 2000


def AddMoney():
    global Money  # <--need to use this otherwise error
    Money = Money + 1

    
print(Money)
AddMoney()
print(Money)

# in above example we defined variable Money in global namespace
# in function money we assigned money a value therefore
# python assumes money as a local variable

# however we accessed the value of the local variable money before
# setting it so an unboundlocalerror is the result

print()
#---------------------------------------------------------
# the dir() function
# returns a sorted list of strings containing the names
# defined by a module

import math  # math module built-in
content = dir(math)
print(content)

print()
#---------------------------------------------------------
# globals() and locals() functions
# can be used to return the names in the global and local
# namespaces depending on the location from where they are 
# called

# if locals() is called from within a function, it will 
# return all the names that can accessed locally from that 
# function

# if globals() is called from within a function, it will 
# return all the names that can accessed globally from that
# function

# return type is dictionary 
# names can be extracted using the keys() function
#---------------------------------------------------------
# the reload() function

# when module is imported into a script the code in the
# top-level portion of a module is executed only once
# to re-execute the top-level code, you have to use the 
# reload() function

# SYNTAX
# reload(module_name)
# reload(hello)         reloads the hello module
#---------------------------------------------------------
# Packages in python
# is a hierarchical file directory structure 

# that defines a single python application environment 
# that consists of modules and sub-packages and 
# sub-sub-packages

# USES POTS.PY               
#            def Pots():
#                print("I'm Pots Phone")

# from Pots import Pots
# from Isdn import Isdn
# from G# import G3

# putting all these functions in __init__.py in the Phone
# directory....they are all available when importing Phone

# Phone.Pots()
# phone.Isdn()
# phone.G3()

# prints the following below:
# I'm Pots phone
# I'm G3 phone
# I'm ISDN phone


#you can make multiple functions in a file
#can also define different python classes in those files
#they can be used to create packages from those classes

print()
#---------------------------------------------------------

