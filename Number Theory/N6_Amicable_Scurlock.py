#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:11:36 2019

@author: Ashley
"""
#%%

def divisor(n):
    div = []
    for i in range(1, int(n/2) + 1):
        if n%i == 0:
            div.append(i)
    #print('The proper divisors of', n ,'are',div)
    return div
    
def amicable(N):
    for n in range(N+1):
        m = sum(divisor(n))
        if sum(divisor(m)) == n:
            print(m,'and',n,'are amicable')


amicable(220)

#%%
def divisor_mod(n):
    div = []
    for i in range(1, int(n/2) + 1):
        if n%i == 0:
            div.append(i)
    return sum(div)%100

def amicable_mod(N):
    for n in range(1,N+1):
        m = divisor_mod(n)
        if divisor_mod(m) == n:
            print(m,'and',n,'are amicable mod 100')

amicable_mod(220)