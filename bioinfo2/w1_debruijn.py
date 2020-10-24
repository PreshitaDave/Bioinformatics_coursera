# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 19:39:51 2020

@author: Presh
"""

#    RIGHT ONE!!!!!!!!
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



def DeBruijn(Text, k):
    node, allkmers = PathGraph(Text, k)
    val = {}
    n = len(node)
    k = len(node[0])
    for i in range(0, n):
        val.setdefault(node[i], [])
        for j in range(0, len(allkmers)): 
            if node[i] == allkmers[j][:k]:
                #if allkmers[j] not in val[node[i]]:
                val[node[i]].append(allkmers[j][1:])
    output(val)    

           
def PathGraph(Text,k):
    edges = []
    edges = Compositionk(Text, k)
    nodes = []
    nodes = Compositionk(Text, k-1)
    nodes1 = list(dict.fromkeys(nodes))   
    nodes1.sort()
    return nodes1, edges

    

Text = "AAGATTCTCTAAGA"
k=4
DeBruijn(Text, k)
