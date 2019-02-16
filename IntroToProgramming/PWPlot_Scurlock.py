#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 12:41:47 2019

@author: Ashley
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

N = 30
x_values = np.linspace(-3, 3,num = N)

def plotting(x_values):
    for x in x_values:
        if x < -2:
            plt.plot([x], [-3 * (x + 2)**2 + 1], 'ro')
        elif (-2 <= x) and  (x < -1):
            plt.plot([x], [1], 'ro')
        elif (-1 <= x) and  (x <= 1):
            plt.plot([x], [(x - 1)**3 + 3], 'ro')
        elif (1 < x) and  (x < 2):
            plt.plot([x], [np.sin(np.pi * x) + 3], 'ro')
        elif x >= 2:
            plt.plot([x], [3 * np.sqrt((x - 2)) + 4], 'ro')


plotting(x_values)   
    