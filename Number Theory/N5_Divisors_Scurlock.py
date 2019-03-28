#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:02:25 2019

@author: Ashley
"""
#%%
def divisor(n):
    div = []
    for i in range(1, int(n/2) + 1):
        if n%i == 0:
            div.append(i)
    print('The proper divisors of', n ,'are',div)
    
divisor(220)


#%%
def divisor_mod(n):
    div = []
    for i in range(1, int(n/2) + 1):
        if n%i == 0:
            div.append(i)
    print('the sum of prop divisors is',sum(div))
    print('he sum of prop divisors mod 100 is',sum(div)%100)
    return sum(div)%100

divisor_mod(220)
    