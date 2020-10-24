# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 13:15:21 2020

@author: Presh
"""
def output(d):
    for k,v in d.items():
        str1 = ","
        v = str1.join(v)
        print(k + " -> " + v)

        
def CompositionGraph(Patterns):
    nodes = []
    n = len(Patterns)
    k = len(Patterns[0])
    for i in range(0, n):
        nodes.append(Patterns[i][:k-1])
        nodes.append(Patterns[i][1:])
        nodes1 = list(dict.fromkeys(nodes))   
        nodes1.sort()
    return nodes1

def DeBruijn_from_kmers(list1):
    node = CompositionGraph(list1)
    val = {}
    n = len(node)
    k = len(node[0])
    for i in range(0, n):
        val.setdefault(node[i], [])
        for j in range(0, len(list1)): 
            if node[i] == list1[j][:k]:
                #if allkmers[j] not in val[node[i]]:
                val[node[i]].append(list1[j][1:])
    output(val)  
    
    
list1 = ["GAGG",
"CAGG",
"GGGG",
"GGGA",
"CAGG",
"AGGG",
"GGAG"]
DeBruijn_from_kmers(list1)
