# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:35:46 2020

@author: Presh
"""
def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern



def Reverse(Pattern):
    reverse = []
    l = len(Pattern)
    for i in range(l):
        rev = Pattern[l-i-1]
        reverse.append(rev)
        final = ''.join(map(str, reverse)) 
    return final
    
    
def Complement(Pattern):
    res1 = Pattern.replace('A','%temp%').replace('T', 'A').replace('%temp%', 'T')  
    res = res1.replace('G','%temp%').replace('C', 'G').replace('%temp%', 'C')
    return res
    
    
p = "AAAACCCGGT"    
a = ReverseComplement(p)
print(a)