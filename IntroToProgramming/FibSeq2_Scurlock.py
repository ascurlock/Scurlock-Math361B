#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 20:38:40 2019

@author: Ashley
"""
#%%
N = 100
m = 30
terms = [0] * N
multiples_m = []


for n in range(N):
    if n == 0:
        terms[0] = 0
    elif n == 1:
        terms[1] = 1
    elif (n != 1) or (n != 2):
        terms[n] = terms[n-1] + terms[n-2]

for i in range(len(terms)):
    if (terms[i] % m == 0):
        multiples_m.append(terms[i])
        if i % 4 == 0:
            print('this is divisible by 4')

#print(terms)
print()
#print("The values ", multiples_m, " are all divisible by ", m)
print("The percentage of even multiples is ",(len(multiples_m)/len(terms))*100)

#%%
#Notes:
#All of the even values are at the indexs that are multiples of 3
#m=3 indexs are multiples of 4 - (4*1) 25%
#m=4 indexs are mltiples of 6  
#m=5 indexs are mltiples of 5  
#m=6 indexs are mltiples of 12  -(4*3) 9%
#m=7 indexs are mltiples of 8  
#m=8 indexs are mltiples of 6  
#m=9 indexs are mltiples of 12 -(4*3) 9%
#m=10 indexs are mltiples of 15
#m=11 indexs are mltiples of 10
#m=12 indexs are mltiples of 12 -(4*3) 9%
#m=13 indexs are mltiples of 7
#m=14 indexs are mltiples of 24
#m=15 indexs are mltiples of 20 -(4*5) 5%
#m=16 indexs are mltiples of 12
#m=17 indexs are mltiples of 9
#m=18 indexs are mltiples of 12 -(4*3) 9%
#m=19 indexs are mltiples of 18
#m=20 indexs are mltiples of 30
#m=21 indexs are mltiples of 8 -(4*2) 13%
#m=24 indexs are mltiples of 12 -(4*3) 9%
#m=27 indexs are mltiples of 36 -(4*3) 3%
#m=30 indexs are mltiples of 60