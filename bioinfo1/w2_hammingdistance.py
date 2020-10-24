# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:35:06 2020

@author: Presh
"""
def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    # your code here
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
            positions.append(i)
            
    return len(positions)



def HammingDistance(p, q):
    count = 0
    if len(p) == len(q):
        for i in range(len(p)):
            if p[i] != q[i]:
                count = count+1
    return count
    
    
    

Pattern = "CCAGTCAATG"
Text = "CCAGTCAATG"
d = 1
a = ApproximatePatternMatching(Text, Pattern, d)
print(a)

p  ="CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG"
q = "ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"
b = HammingDistance(p,q)