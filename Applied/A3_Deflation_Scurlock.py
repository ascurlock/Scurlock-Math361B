#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 12:05:24 2019

@author: Ashley
"""
#%%
#define the polynomial f lowest power first
f = [-1,0,0,1]
#define the polynomial g liwest power first
g = [2,1]

import numpy as np

def clean_poly(p):
    highest_deg = len(p) - 1   
    for ii in range(len(p)-1,-1,-1):
        if np.abs(p[ii]) > 1e-15:
            break
        else:
            highest_deg -= 1      
    del p[highest_deg+1:]
    return p

def polydiv(f, g):
    r = f
    q = [0] * ((len(r) - len(g)) + 1)
    qq = 1
    while r != [0] and (len(g)-1 <= len(r)-1):
        #Finding q
        q1 = [0] * ((len(r) - len(g)) + 1)
        q1[-1] = r[-1]/g[-1]
        q[-qq] = q1[-1]
        qq = qq +1
        #Finding r
        r1 = [0] * (len(q1) + 1) # + (len(g) - 1))
        for ii in range(len(q1)):
            for jj in range(len(g)):
                r1[ii + jj] = r1[ii + jj] + q1[ii]*g[jj]
        r = clean_poly([x - y for x, y in zip(r, r1)])
    return ('f =' + str(f) + ', g=' + str(g) + ', r=' + str(r) + ', q=' + str(q))