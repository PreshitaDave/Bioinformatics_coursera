# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 19:59:23 2020

@author: Presh
"""

def MinimumSkew(Genome):
    # generate an empty list positions
    positions = []
    # set a variable equal to SkewArray(Genome)
    skew1 = SkewArray(Genome)
    b = min(skew1)
    # find the minimum value of all values in the skew array
    for i in range(len(skew1)):
        if skew1[i] == b:
            positions.append(i)
    # range over the length of the skew array and add all positions achieving the min to positions
    return positions

#skew array 
def SkewArray(Genome):
    skew = [0]
    for i in range(len(Genome)):
        if Genome[i] == 'A' or Genome[i] == 'T':
            skew[i] = skew[i-1]
        elif Genome[i] == 'G':
            skew[i] = skew[i] + 1
        else: 
            skew[i] = skew[i] - 1
        skew.append(skew[i])
    skew[:0] = [0]
    skew.pop(-1)
    return skew


        
Text = "CATTCCAGTACTTCGATGATGGCGTGAAGA"
a = MinimumSkew(Text)
print(a)
