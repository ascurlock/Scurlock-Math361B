#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:52:38 2019

@author: Ashley
"""
#%%
import math

def zero_devisor(m):
    zero_divs = []
    for i in range(1,m):
        for j in range(1,m):
            if (i*j)%m == 0:
#                print(i, '*',j,'=',i*j, 'is divisible by',m)
                if i not in zero_divs:
                    zero_divs.append(i)
                if j not in zero_divs:
                    zero_divs.append(j)
    return str(m) + ' has ' + str(len(zero_divs)) + ' Zero Divisors: ' + str(sorted(zero_divs))


zero_devisor(15)

#%%