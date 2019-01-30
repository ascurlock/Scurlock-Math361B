#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:04:42 2019

@author: Ashley
"""
#%%
#Initialize Values
x = 1
y = 1
z = 1
mylist = []

mylist.append(x + y) #first component
mylist.append((y * z) + (3 * x)) #second component
mylist.append(mylist[0]**2) #third component
mylist.append((2*mylist[1] - x/2)/mylist[0])#fourth component
mylist.append(7%3)#fifth component

mylist[2] = mylist[2] + 3
mylist[-1] = mylist[-1] * (3/4)

print('The final values in the list are: ', mylist)
print('The sum of all of the components in this list is ', mylist[0] + mylist[1] + mylist[2] + mylist[3] + mylist[4])