'''
Created on Jan 30, 2018

@author: shifa
'''
#Random Number Functions

#choice(seq)
import random
 
print("Choice returns random item from list/tuple/string.")
print()
print("random number from range(100):", random.choice(range(100)))
print("random element from list[1,2,3,5,9]:", random.choice([1,2,3,5,9]))
print("random character from string 'Hello World':", random.choice('Hello World'))
 
#also works with the following:
list2 = [100,1001,45,23]
print(random.choice(list2))
print()
#----------------------------------------
#randrange([start,] stop [,step]) function
#start default is 0
#stop default is 1
#uses import random

print("randrange(1,100,2):", random.randrange(1,100,2))
#randomly select an odd number between 1-100

print("randrange(100):", random.randrange(100))
#randomly select a number between 0-99

print()
#----------------------------------------
#uses import random
#this method returns a random float r 
#0.0 <= r <= 1.0
#random() returns floating point number in range [0.0,1.0]

print("random():", random.random())
#random number

print("random():", random.random())
#second random number 

print()
#-----------------------------------------
#initializes the basic random number generator
#seed([x],[y]) 
#x is seed for next random number; if int then used directly
#y- default is 2; str/byte/byte array object gets converted
#in int

random.seed()
print("random number with default seed", random.random())
random.seed(10)
print("random number with int seed", random.random())
random.seed("hello",2)
print("random number with string seed", random.random())

print()
#------------------------------------------
#shuffle() - randomizes the items of a list in place
#shuffle(lst, [random])
#lst can be list or tuple
#random is optional 0 argument return float between 0.0-1.0
#default is none for random

#need to call function using random static object
#returns reshuffled list

#uses import random

list1 = [20,16,10,5]
random.shuffle(list1) 
print("Reshuffled list:", list1)

random.shuffle(list1)
print("Reshuffled list:", list1)

print()
#---------------------------------------------
#uniform(x,y) returns a random float r 
#such that x is less than or equal to r
#and r is less than y

#x sets the lower limit of random float
#y sets the upper limit of random float
#x <= r < y

#uses import random

print("Random Float uniform(5,10):", random.uniform(5,10))
print("Random Float uniform(7,14):", random.uniform(7,14))

print()
#----------------------------------------------










