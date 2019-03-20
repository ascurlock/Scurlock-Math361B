#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 23:18:48 2019

@author: Ashley
"""
#%%
import numpy as np
import math

x = 3

def prime_check(value):
    if value == 1:
        return False
    if value == 2:
        return True
    for small in range(2, math.floor(np.sqrt(value) + 1)):
        if value%small == 0:
            return False
    else:
        return True


def gold_calc(value):
    if prime_check(value):
        return True
    for i in reversed(range(math.floor(np.sqrt(value)))):
       if value - 2*(i**2) > 0 and prime_check(value - 2*(i**2)): 
#           print(str(value) + ' = ' + str(value - 2*(i**2)) + '*(2*' + str(i) + '^2)')
           return True
    return False

while gold_calc(x):
    x = x + 2
print(x, "can't be written as the product of a prime and twice a square.")




#%%




