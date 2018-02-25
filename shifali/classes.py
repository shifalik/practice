'''
Created on Feb 14, 2018

@author: shifa
'''

# CLASSES
#---------------------------------------------------------
# creating a class format

# class ClassName:
#    'Optional class documentation string'
#    class_suite
#---------------------------------------------------------

    
class Employee:
    'Common base class for all employees'
    empCount = 0

# empCount is class variable whose value is shared among
# all the instances of a in this class

# Employee.empCount can be accessed from inside/outside class

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
# __init__() is special method -->called constructor/initialization method
# double underscore each side to initialize
        
    def displayCount(self):
        print("Total Employees %d" % Employee.empCount)
        
    def displayEmployee(self):
        print("Name:", self.name, ",Salary:", self.salary)        
        
# declare other class method like normal functions with 
# the exception that the first argument to each method 
# is self
#---------------------------------------------------------
# creating instance objects
# call the class using class name and pass in whatever
# arguments its _init_ method accepts


# Objects of Employee class.
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp3 = Employee("Santa", 4000)

#---------------------------------------------------------
# accessing attributes
# can access object's attributes using the dot operator 
# with object

emp1.displayEmployee()
emp2.displayEmployee()

emp3.displayEmployee()
print("Total Employees %d" % Employee.empCount)

#---------------------------------------------------------
# ADD/REMOVE/MODIFY attributes of classes and objects
# at any time

# emp1.age = 27 #adding a 'age' attribute
# emp1.name = 'xyz' #modify 'name' attribute
# del emp1.salary #delete 'salary' attribute

print()
print("Checking for Salary Attributes")
print("For: Emp1")

# checking to see if an attribute exists or not
# true or false response
a = hasattr(emp1, 'salary')
print(a)

# Accessing the attribute of object
# gives value of 'salary'
b = getattr(emp1, 'salary')
print(b)

# Setting an attribute 
# if non-existent then one is created
c = setattr(emp1, 'salary', 7000)
print(c)

# Deleting an attribute
d = delattr(emp1, 'salary')
print(d)

print()
#--------------------------------------------------------
# Built-In Class Attributes

print("Employee.__doc__:", Employee.__doc__)    
# class documentation

print("Employee.__name__:", Employee.__name__)  
# class name

print("Employee.__module__:", Employee.__module__)  
# module name in which the class is defined
# #it is __main__ in interactive mode

print("Employee.__bases__:", Employee.__bases__)
# possibly empty tuple containing the base classes
# in the order of their occurrence in the base class list

print("Employee.__dict__:", Employee.__dict__)
# dictonary containing the class's namespace

print()
#---------------------------------------------------------
# Destroying Objects- Garbage Collection
# runs during program execution and triggered when an
# object's reference count reaches zero <--python collects automatically

# object's reference increases when assigned new name or 
# placed in container (list/tuple/dict)

# object's reference decreases when it is deleted, reassigned,
# or its reference goes out of scope 

a = 40  # object created 
b = a  # increase ref count
c = [b]  # increase ref count

del a  # dec ref count
b = 100  # dec ref count    
c[0] = -1  # dec ref count

#---------------------------------------------------------
# Using __del__ destructor

# class Point:
#     
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y
# 
#     def __del__(self):
#         class_name = self.__class__.__name__    
#         print(class_name, "destroyed")
# 
# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# print(id(pt1), id(pt2), id(pt3))
# del pt1
# del pt2
# del pt3

# importing above from point.py file

# import point
# p1 = point.Point()

print()
#--------------------------------------------------------
# Class Inheritance
# child class inherits the attributes of its parent class

# can do so by listing the parent class in parentheses
# after the new class name

# child class gets attributes of parent class, can override
# data and methods from the parent

# FORMAT
# class SubClassName (ParentClass1[ , ParentClass2, ...]):
#    'Optional class documentation string'
#    class_suite


class Parent:  # parent class
    parentAttr = 100
    
    def __init__(self):
        print("Calling parent constructor")
    
    def parentMethod(self):
        print("Calling parent method")
        
    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute:", Parent.parentAttr)


# self below
p = Parent()
p.parentMethod()
#p.setAttr(500)
p.getAttr()
print()
# self end


class Child(Parent):  # define child class
    
    def __init__(self):
        print("Calling child constructor")
        
    def childMethod(self):
        print("Calling child method")

        
c = Child()  # instance of child
c.childMethod()  # child calls its method
c.parentMethod()  # calls parent method
c.setAttr(200)  # again calls parent method
c.getAttr()  # again calls parent method

#--------------------------------------------------------
#can drive a class from multiple parent classes

#class A: ...
#class B: ...
#class C(A,B): ...    subclass of A and B

print()
#---------------------------------------------------------
#issubclass(sub,sup)
#boolean response T/F
#true is the given sub is indeed a subclass of the 
#superclass sup

b = issubclass(Child, Parent)
print("Child a subclass of Parent:", b)

#isinstance(obj,Class)
#boolean response T/F
#obj is an instance of Class or an instance of 
#subclass of Class


a = isinstance(c, Parent)        
print("C instance of Subclass Parent:", a)

print()
#---------------------------------------------------------
print("Overriding Methods")
#can override parent class methods

#mostly do it because you want special/different 
#functionality in the subclass

class ParentOne:    #defining parent class
    
    def myMethod(self):
        print('Calling parent method')

class ChildOne (ParentOne): #defining child class
    
    def myMethod(self):
        print("Calling child method")

c = ChildOne()     #instance of child
c.myMethod()    #child class overridden method
    
print()
#---------------------------------------------------------
#Base Overloading Methods

#__init__(self [,args..])       constructor with arguments
#obj = className(args)

#__del__(self)                  destructor, delete object
#del obj

#__repr__(self)                 evaluatable string representation
#repr(obj)

#__str__(self)                  printable string representation
#str(obj)

#__cmp__(self,x)                object comparison
#cmp(obj,x)

#---------------------------------------------------------
#Overloading Operators

class Vector:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return 'Vector(%d, %d)' % (self.a, self.b)
    
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1 + v2)

print()
#---------------------------------------------------------
print("Data Hiding")
#objects attributes may or may not be visible outside 
#class definition

#need to name attributes with double underscore prefix
#those attributes not be directly visible to outsiders 

class JustCounter:
    __secretCount = 0       #_ _ strictly private
    
    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
#print(counter._secretCount)
#gives Attribute error as it should 


print(counter._JustCounter__secretCount)
#write this above to access attributes 
#should print 1 2 2 

#python protects members by internally changing the name to 
#include the class name
#---------------------------------------------------------




