#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 23:15:23 2019

@author: Ashley
"""
#%%
import math

def inverses(m):
    mult_inv = []
    for i in range(2,m):
        for j in range(2,m):
            if (i*j-1)%m == 0:
#                print(i*j ,i, 'and',j,'are inverses in mod',m)
                if i not in mult_inv:
                    mult_inv.append(i)
                if j not in mult_inv:
                    mult_inv.append(j)
    return str(m) + ' has ' + str(len(mult_inv)) + ' Inverses: ' + str(sorted(mult_inv))


inverses(15)

#%%