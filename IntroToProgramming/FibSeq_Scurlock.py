#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 12:13:11 2019

@author: Ashley
"""
#%%
F0 = 5 #starting value 1
F1 = 6 #starting value 2
N = 10 #Number of terms in a sequence
terms = [0] * N

cass1 = 0
cass2 = 0
cassID = []


for n in range(N):
    if n == 0:
        terms[0] = F0
    elif n == 1:
        terms[1] = F1
    elif (n != 1) or (n != 2):
        terms[n] = terms[n-1] + terms[n-2]
print("The lst 10 terms in the sequence are ", terms[-10:])

print()
#Testing Cassini's Identity 
for n in range(1, len(terms)-1):
    cass1 = terms[n]**2 - (terms[n-1] * terms[n+1])
    cass2 = (-1)**(n-1)
    if cass1 == cass2:
        cassID.append(True)
    else:
        cassID.append(False)
#        print("cass1 = ",cass1, " and cass2 = ", cass2) 
    
print("The results of the Cassini's Identity from assignment is ", cassID)


