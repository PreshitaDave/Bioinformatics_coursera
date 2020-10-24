# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:01:24 2020

@author: Presh
"""

def Compositionk(Text, k):
    freq = []
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq.append(Pattern)
    freq.sort()
    return freq
        
Text = "CAATCCAAC"
k=5
b = Compositionk(Text, k)
print(b)
