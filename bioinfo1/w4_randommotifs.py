# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 20:35:33 2020

@author: Presh
"""
import random

def RandomMotifs(Dna, k, t):
    randmot = []
    l = len(Dna[0])
    for i in range(t):
        r = random.randint(1, l-k)
        r1 = Dna[i][r:r+k]
        randmot.append(r1)
    return randmot


