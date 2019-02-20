# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
import numpy as np
import math

n = 11
prime_numbers = []
ii = 2

#Checker that returns True if a value is prime and False if not
def prime_check(value):
    #Checks when Value = 1
    if value == 1:
        return False
    #Checks if the value is even
    if value == 2:
        return True
    #check to see if the value is divisible by a smaller value
    for small in range(2, math.floor(np.sqrt(value) + 1)):
        if value%small == 0:
            return False
    else:
        return True

#To determine the nth prime number
while len(prime_numbers) < n:
    if prime_check(ii):
        prime_numbers.append(ii)
    ii = ii + 1
print("The ", n ,"th prime number is ", prime_numbers[-1])
        
##Of the values 1-n which values are prime
#for i in range(1,n+1):
#    if prime_check(i):
#        print(str(i) + " is prime")