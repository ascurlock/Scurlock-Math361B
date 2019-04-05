#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:15:03 2019

@author: Ashley
"""
#%%
import numpy as np
import math
prime = 17

def prime_check(value):
    #Checks when Value = 1
    if value == 1:
        return False
    #Checks if the value is even
    if value == 2:
        return True
    #check to see if the value is divisible by a smaller value
    for small in range(2, math.floor(np.sqrt(value) + 1)):
        if value%small == 0:
            return False
    else:
        return True

def quad(P):
    count = []
    counts = np.zeros([0,2])
    counts = np.vstack( [counts, np.array(['Prime', 'Number of Quad residues'])] )
    for p in range(0,P+1):
        if prime_check(p):
            for ii in range(p):
                if (ii * ii)%p not in count:
                    count.append((ii * ii)%p)
            counts = np.vstack( [counts, np.array([p, len(count)])] )
    return counts
            
print('The number of quadratic residues for each prime less than',prime,'is \n',quad(prime))
print('')
def quad_neg1(P):
    count = []
    counts = np.zeros([0,2])
    counts = np.vstack( [counts, np.array(['Prime', 'is -1 a Quad residue?'])] )
    for p in range(1,P+1):
        if prime_check(p):
            for ii in range(p):
                if (ii * ii)%p not in count:
                    count.append((ii * ii)%p)
            if (p-1) in count:
                counts = np.vstack( [counts, np.array([p, 'True'])] )
            else:
                counts = np.vstack( [counts, np.array([p, 'False'])] )
    return counts

print('For each prime less than',prime,'is -1 a quadratic residue \n',quad_neg1(prime))