#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:02:18 2019

@author: Ashley
"""
#%%
import numpy as np
import math

N= 2 #max iterations
n = 100
TOL = 0.0001 #tolerance
z0 = 4.837 #Initil iterte
#f = lambda x: .01*(x**4 + 
#              (np.e - 2 - np.sqrt(2))*x**3 + 
#              (2*np.sqrt(2) - np.sqrt(2)*np.e - 3 - 2*np.e)*x**2 + 
#              (2*np.sqrt(2)*np.e + 3*np.sqrt(2) - 3*np.e)*x + 
#              (3*np.sqrt(2)*np.e))
#ff = lambda x: .01*(4*x**3 + 
#              3*(np.e - 2 - np.sqrt(2))*x**2 + 
#              2*(2*np.sqrt(2) - np.sqrt(2)*np.e - 3 - 2*np.e)*x + 
#              (2*np.sqrt(2)*np.e + 3*np.sqrt(2) - 3*np.e))
f = lambda x: math.tan(x) + x - 2
ff = lambda x: 1/(math.cos(x))**2 + 1
allIterations = [z0]
allDifferences = []
found = False

while n <= 100:
    z1 = z0 - (f(z0) / ff(z0))
    allIterations.append(z1)
    allDifferences.append(abs(z1 - z0))
    if abs(z1 - z0) < TOL:
        print('The function converges')
        print('The iterations are: \n',allIterations,'\n')
        print('The spacing between iterations are: \n',allDifferences)
        found = True
        break
    else:
        z0 = z1
        
if found == False:
    print('The function diverges')
    print('The iterations are: \n',allIterations,'\n')
    print('The spacing between iterations are: \n',allDifferences)
    
    
#%%