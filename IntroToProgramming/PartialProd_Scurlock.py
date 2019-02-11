#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:14:02 2019

@author: Ashley
"""
#%%
import numpy as np
N=95500
pn_values = np.empty([N])
pn = 1


#First function
for ii in range(2,N+1):
    pn *= (ii**3 - 1)/(ii**3 + 1) 
    pn_values[ii-2] = pn

print("The first 15 values of pn are ", pn_values[:15])
print()
print("The last 15 values of pn are ", pn_values[-45:])


#%%
N=31
qn_values = np.empty([N])
qn = 1

#Second Function
for ii in range(1,N+1):
    qn *= np.exp((ii/100))/ii**10
    qn_values[ii-1] = qn

print("The first 15 values of qn are ", qn_values[:15])
print()
print("The last 15 values of qn are ", qn_values[-15:])

#%%
N=710
an_values = np.empty([N])
an = 1
##Third Function of my choice :)
for ii in range(1,N+1):
    an *= (ii**np.e - np.exp((ii)))/(np.exp((ii)) + ii**np.e) + 2
    an_values[ii-1] =  an

print("The first 15 values of qn are ", an_values[:15])
print()
print("The last 15 values of qn are ", an_values[-15:])

#%%
