# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 19:01:13 2020

@author: Presh
"""
def output(d):
    for k,v in d.items():
        str1 = ","
        v = str1.join(v)
        print(k + " -> " + v)


def Overlap(pattern):
    val = {}
    n = len(pattern)
    for i in range(0, n):
        for j in range(0, n): 
            if pattern[i][1:] == pattern[j][:4]:
                val.setdefault(pattern[i], [])
                val[pattern[i]].append(pattern[j])
    output(val)
    
pattern = ["ATGCG",
"GCATG",
"CATGC",
"AGGCA",
"GGCAT",
"GGCAC"]

a = Overlap(pattern)

