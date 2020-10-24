# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 10:57:15 2020

@author: Presh
"""
# WRONG ONE
def output(d):
    for k,v in d.items():
        str1 = ","
        v = str1.join(v)
        print(k + " -> " + v)

def Compositionk(Text, k):
    freq = []
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq.append(Pattern)
    freq.sort()
    return freq

def Overlap(pattern):
    val = {}
    n = len(pattern)
    for i in range(0, n):
        for j in range(0, n): 
            if pattern[i][1:] == pattern[j][:k-2]:
                val.setdefault(pattern[i], [])
                val[pattern[i]].append(pattern[j])
    output(val)

def DeBruijn(Text, k):
    nodes = PathGraph(Text, k)
    Overlap(nodes)
    
           
def PathGraph(Text,k):
    #edges = []
    #edges = Compositionk(Text, k)
    nodes = []
    nodes = Compositionk(Text, k-1)
    nodes1 = list(dict.fromkeys(nodes))   
    nodes1.sort()
    return nodes1
    

Text = "AAGATTCTCTAAGA"
k=4
DeBruijn(Text, k)