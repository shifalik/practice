'''
Created on Feb 25, 2018

@author: shifa
'''


list = [100, 24, 23, 76, 56, 22, 10, 96, 76]

for x in range(len(list)):
    
    for y in range(x+1, len(list)):
        if not(list[x] <= list[y]):
            a = list[y]
            list.pop(y)
            list.insert(x, a)
            #print(list)
        #else:
            #print(list)
print('sorted list',list)


