#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 12:10:39 2019

@author: Ashley
"""
#%%
#Solves a polynomial 'p' at a given point 'point'
def polypoint(p, point):
    solution = 0
    for i in range(len(p)):
        solution = solution + (p[i]*point**i)
    return solution

#Prints out a readable polynomial when passed a list of coefficients 
    #starting with the smallest power
def name(p):
    values = ''
    for i in range(len(p)):
        if i == 0:
            values = values + '+(' + str(p[i]) + ')'
        elif p[i] == 0:
            values = values
        else:
            values = values+ '+(' + str(p[i]) + 'x^' + str(i) + ')'
    return values
        
#Finds the derivative of a polynomial when passed a list
    # of coefficients and returns the derivatve as a list of coefficients
def deriv(p):
    derivative = []
    for i in range(1,len(p)):
            derivative.append(p[i]*i)
    return derivative
        
#Calculates the definite integral of polynomial 'p' in the range a to b
    # where a is the start value and b is the end value
def integral(p,a,b): #a-Starting value b-Ending value
    integrals = []
    integrals.append(0)
    for i in range(len(p)):
            integrals.append((p[i]/(i+1)))
    return polypoint(integrals, b) - polypoint(integrals, a)


#%%
p = [8,-9,0,-3,4] #polynomial written as a list of coefficients. Lowest power first
c = 5 #point
a = 1 #Integral starting point
b = 2 #Integral ending point

print('f(x)=',name(p))
print('f(' + str(c) + ')='+ str(polypoint(p,c)))
print('f`(' + str(c) + ')=' + str(polypoint(deriv(p),c)))
print('The integral of f(x) from '+str(a)+ ' to ' + str(b) + ' is ' + str(integral(p,a,b)))


