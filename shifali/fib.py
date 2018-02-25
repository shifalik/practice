'''
Created on Feb 21, 2018

@author: shifa
'''
#IN REFERENCE WITH MODULES

#FIBONACCI NUMBERS MODULE

def fib(n):
    result = []
    a,b = 0,1
    while b < n:
        result.append(b)
        a, b = b , a + b
    return result

#executing modules as scripts (add-on part seen below)

if __name__ == "__main__":
    f = fib(100)
    print(f)
