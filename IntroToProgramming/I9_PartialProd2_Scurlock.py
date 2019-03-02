#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 12:08:06 2019

@author: Ashley
"""
#%%
import numpy as np
#Example
N = 96 #Numbers of rerms in a partial product sequence

a_n = lambda n: n**2 + 9*n - 7

pn_values = np.empty([N])
pn = 1

#Function
for ii in range(0,N):
    pn *= a_n(ii)
    pn_values[ii] = pn

print("The first 15 values of pn are ", pn_values[:15])
print()
print("The last 15 values of pn are ", pn_values[-15:])

#%%
#(1)
N = 1000
f_n = lambda n: n**2 + n -3
g_n = lambda n: n**5 + 3*n -2
en_values = np.empty([N])
en = 1

#Function
for ii in range(1,N):
    en *= 1 + (f_n(ii)/g_n(ii))
    en_values[ii] = en
    
print("The first 15 values of pn are ", en_values[:15])
print()
print("The last 15 values of pn are ", en_values[-15:])

#%%
import numpy as np
#(2)
N = 32
b = .5
an_values = np.empty([N])
an = 1

#Function
for ii in range(0,N):
    an *= 1 + b**ii
    an_values[ii] = an

if isinstance(b ,float):
    print("The function converges")
else:
    print("The function diverges")
    
print()
print("The first 15 values of pn are ", an_values[:15])
print()
print("The last 15 values of pn are ", an_values[-15:])