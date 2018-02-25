'''
Created on Feb 20, 2018

@author: shifa
'''

# Dictionary

# each key is separated by its value by :
# items separated by ,
# uses { }

# key are unique, values may not be
# keys must be an immutable data type: strings/numbers/tuples
# values can be any type
#-----------------------------------------------------------
# Accessing Values in Dictionary

dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("dict1['Name']:", dict1['Name'])
print("dict1['Age']:", dict1['Age'])

# print("dict1['Alice']:", dict1['Alice'])
# gives error as it should since Alice is not a part of the
# dictionary 

print()
#-----------------------------------------------------------
# Updating Dictionary

dict2 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict2['Age'] = 8  # update
dict2['School'] = "DPS School"  # new entry 

print("dict2['Age']:", dict2['Age'])
print("dict2['School']:", dict2['School'])

print()
#-----------------------------------------------------------
# Delete Dictionary Elements
# can remove individual dictionary elements or 
# clear the entire contents of a dictionary 

dict3 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict3['Name']  # removes entry with key 'Name'
dict3.clear()  # removes all entries
del dict3  # deletes entire dict

# print("dict3['Age']:", dict3['Age'])
# print("dict3['School']:", dict3['School'])
# above produces error as it should b/c del dict3 was used
# dict3 does not exist no more

print()
#-----------------------------------------------------------
# Properties of Dictionary Keys

# dict values have no restrictions
# dict keys have restrictions

# keys: A and B
# A: no duplicate key is allowed

# ex of A
dict4 = {'Name':'Zara', 'Age': 7, 'Name': 'Manni'}
print("dict4['Name']:", dict4['Name'])

# the last assignment wins so its prints Manni for name

# keys:
# B: keys must be immutable: can use strings/numbers/tuples 
# can not use ['key']

# ex of B
# dict5 = {['Name']: 'Zara', 'Age': 7}
# print("dict5['Name']:", dict5['Name'])
# will produce error as expected because using [] is not 
# allowed --error is that list objects are unhashable

print()
#---------------------------------------------------------
# Built in Dictionary Functions and Methods
# functions

# cmp(dict1,dict2) -->no longer available in Python 3
#---------------------------------------------------------
print("len(dict)") 
# gives total length of dict; 
# equal to number of items in dict

dict6 = {"Name": 'Manni', 'Age': 7, 'Class': 'First'}
print("dict6:", dict6)
print("Length: %d" % len(dict6))

print()
#---------------------------------------------------------
print("str(dict)")
# gives printable string representation of a dictionary

dict6 = {"Name": 'Manni', 'Age': 7, 'Class': 'First'}
print("Equivalent String: %s" % str(dict6))

print()
#---------------------------------------------------------
print("type(variable)")
# returns the type of passed variable 
# if passed dict then return dict type

dict6 = {"Name": 'Manni', 'Age': 7, 'Class': 'First'}
print('Variable Type: %s' % type(dict6))

# str1 = 'hello'
# print("type %s" %type(str1))
# yes prints type <class 'str'>

print()
#---------------------------------------------------------
# Methods
#---------------------------------------------------------
print("dict.clear()")
# removes all items from the dictionary

dict7 = {'Name': 'Zara', 'Age': 7}
print("Start Len: %d" % len(dict7))

dict7.clear()
print("End Len: %d" % len(dict7))

print()
#---------------------------------------------------------
print("dict.copy()")
# returns a shallow copy of the dictionary

dict8 = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
dict9 = dict8.copy()
print("New Dictionary:", dict9)

print()
#---------------------------------------------------------
print("dict.fromkeys(seq [,value]))")
# creates a new dictionary with keys from seq 
# and values set to value

# seq is the list of values 
# value optional if provided then value set to this value

seq = ('name', 'age', 'sex')

dict10 = dict.fromkeys(seq)
print("New Dictionary: %s" % str(dict10))

dict11 = dict.fromkeys(seq, 10)
print("New Dictionary: %s" % str(dict11))

print()
#---------------------------------------------------------
print("dict.get(key, default = None)")
# returns a value for the given key
# for key key, returns value or default if key not in dict

# key to be searched in the dict
# default is value to returned in case key does not exist

dict12 = {'Name': 'Zara', 'Age': 27}

print("Value: %s" % dict12.get('Age'))
print("Value: %s" % dict12.get('Sex'))
print("Value: %s" % dict12.get('Sex', "NA"))

print()
#---------------------------------------------------------
# print("dict.has_key(key)")
# true if available
# false if not available

# dict12 = {'Name': 'Zara', 'Age': 27}
# print('Value: %s' % dict.has_key('Age'))
# print('Value: %s' % dict.has_key('Sex'))

# removed, use the in operation instead
#----------------------------------------------------------
print("dict.items()")
# returns a list of dict's (key,value) tuple pairs

dict12 = {'Name': 'Zara', 'Age': 7}
print("Value: %s" % dict12.items())

print()
#----------------------------------------------------------
print("dict.keys()")
# returns list of all available keys in dictionary 

dict12 = {'Name': 'Zara', 'Age': 7}
print("Value: %s" % dict12.keys())

print()
#---------------------------------------------------------
print("dict.setfault(key,default = None")
# similar to get() but will set dict[key] = default if key
# is not already in dict

# key- key to be searched
# default - value to retruned in case key is not found

dict12 = {'Name': 'Zara', 'Age': 7}
print("Value: %s" % dict12.setdefault('Age', None))
print("Value: %s" % dict12.setdefault('Sex', None))
print(dict12)

print()
#---------------------------------------------------------
print("dict.update(dict2)")
# adds dictionary dict2's key-values pairs to dict
# doesn't return anything

dict12 = {'Name': 'Zara', 'Age': 7}
print("Dict12: ", dict12)
dict13 = {'Sex': 'Female'}

dict12.update(dict13)
print("Updated Dict12: ", dict12)

print()
#---------------------------------------------------------
print("dict.values()")
# returns list of all the values available in dictionary 

dict14 = {'Sex': 'Female', 'Age': 7, 'Name': 'Zara'}
print("Value: ", list(dict14.values()))

print()
#---------------------------------------------------------

