#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:32:21 2019

@author: Ashley
"""
#%%
import matplotlib.pyplot as plt

def string(D0, n):
    m = 0
    a = 'aRbFR'
    b = 'LFaLb'
    D0 = sum([list(x) for x in list(D0)], [])
    while m < n:
        D0 = [a if x == 'a' else b if x == 'b' else x for x in list(D0)]
        D0 = [list(x) for x in list(D0)]
        D0 = sum(D0, [])
        m = m + 1
    return D0

def points(list_of_letters):
    x_values, y_values = [0], [0]
    start, position = 0, [0,0]
    x = [0,1,0,-1]
    y = [1,0,-1,0]
    for i in list_of_letters:
        if i == 'F':
            position[0] = position[0] + x[start]
            position[1] = position[1] + y[start]
            x_values.append(position[0])
            y_values.append(position[1])
        if i == 'R':
            if start == 3:
                start = 0
            else:
                start = start + 1
        if i == 'L':
            if start == 0:
                start = 3
            else:
                start = start - 1
    return [x_values, y_values]

def connectpoints(x,y):
    for ii in range(len(x)-1):
        px, py = x[ii], y[ii]
        nx, ny = x[ii+1], y[ii+1]
        plt.plot([px,nx],[py,ny],'k-')
        
#%%
D0 = 'Fa'
n = 10

x_and_y = points(string(D0, n))
x = x_and_y[0]
y = x_and_y[1]

connectpoints(x,y)

plt.axis('equal')
plt.show()

