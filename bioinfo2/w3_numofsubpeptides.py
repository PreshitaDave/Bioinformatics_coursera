# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:50:52 2020

@author: Presh
"""

def numofsubpeptides(n):
    a = n*(n-1)
    return a 

n = 4
b = numofsubpeptides(n)
print(b)

def subpeptidesinlinear(n):
    a = 1
    for i in range(0, n):
        a += n-i
    return a 

c = subpeptidesinlinear(4)
print(c)