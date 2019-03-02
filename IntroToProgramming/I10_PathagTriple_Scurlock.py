#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:45:52 2019

@author: Ashley
"""

#%%
import numpy as np
matrix = np.zeros([0,4])
matrix = np.vstack( [matrix, np.array(['a','b','c','a+b+c'])] )

N = 310

for ii in range(1, N):
    for jj in range(ii,N):
        if (np.sqrt(ii**2 + jj**2)).is_integer() == True:
            matrix = np.vstack([matrix, np.array([ii,jj,int(np.sqrt(ii**2 + jj**2)), ii + jj + int(np.sqrt(ii**2 + jj**2))])] )
            if (ii + jj + int(np.sqrt(ii**2 + jj**2))) == 1026:
                print("The pythagorean triple that sums to 1026 is a=" + str(ii) + " b=" + str(jj) + " and c=" + str(int(np.sqrt(ii**2 + jj**2))))
