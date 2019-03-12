#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:56:58 2019

@author: Ashley
"""
#%%
collatz_list = [0]

def collatz(a0, N):
    collatz_list[0] = a0
    for ii in range(N):
        #value equals 1
        if collatz_list[ii] == 1:
            print('After', len(collatz_list), 'terms', a0, 'reached 1')
            return collatz_list
        #even
        if collatz_list[ii]%2 == 0:
            collatz_list.append(collatz_list[ii]/2)
        #odd
        elif collatz_list[ii]%2 != 0:
            collatz_list.append((3 * collatz_list[ii]) + 1)
    print('After ', len(collatz_list), ' terms we did not reach 1')
    return collatz_list

collatz(10, 25)