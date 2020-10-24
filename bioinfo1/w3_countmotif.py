# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:47:57 2020

@author: Presh
"""


def Score(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])  
    res = Consensus(Motifs)
    s2 = 0
    
    for j in range(k):
            s1 = 0
            for l in range(0, t):
                if Motifs[l][j] != res[j] :
                    s1 += 1
            s2 += s1
    return s2
    
def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus
    

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    # insert your code here
    profile = Count(Motifs)
    for i in profile.keys():  
        for j in range(k):
            profile[i][j] = profile[i][j]/t      
        
    return profile

def Count(Motifs):
    count = {} # initializing the count dictionary
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
             
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
             
    return count

Motifs = ["AACGTA","CCCGTT","CACCTT","GGATTA","TTCCGG"]
b = Score(Motifs)
print(b)
