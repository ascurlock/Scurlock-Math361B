#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:14:02 2019

@author: Ashley
"""
#%%
import numpy as np
N=65500
sn_values = np.empty([N])
sn = 0

#First function
for ii in range(1,N+1):
    sn += np.log((ii**4 + ii + 3))/(ii**.5 + 3)
    sn_values[ii-1] = round(sn,2)

print("The first 15 values of sn are ", sn_values[:15])
print()
print("The last 15 values of sn are ", sn_values[-15:])
print()

#%%
N=70978
tn_values = np.empty([N])
tn = 0
#Second Function
for ii in range(1,N+1):
    tn += np.exp((ii/100))/(ii**10)
    tn_values[ii-1] = tn

print("The first 15 values of tn are ", tn_values[:15])
print()
print("The last 15 values of tn are ", tn_values[-15:])

tn_values.max()

#%%
import numpy as np
N=27500
an_values = np.empty([N])
an = 0
#Third Function of my choice
for ii in range(1,N+1):
    an += (-1)**ii/(ii**0.6)
    an_values[ii-1] = round(an,2)

print("The first 15 values of an are ", an_values[:15])
print()
print("The last 15 values of an are ", an_values[-15:])

