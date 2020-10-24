# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:19:29 2020

@author: Presh
"""

def PathToGenome(path):
    text = path[0]
    n = len(path)
    #k = len(path[0])
    for i in range(1, n):
        text += path[i][-1]
    return text


path = ["ACCGA","CCGAA","CGAAG","GAAGC","AAGCT"]
a = PathToGenome(path)
print(a)