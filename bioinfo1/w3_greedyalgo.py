# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:55:00 2020

@author: Presh

"""
# to find probability of consensus sequence
def Pr(Text, Profile):
    pr = 1
    k = len(Profile['A'])
    for i in range(0, k): 
        pr1 = 1
        for l in Profile.keys():
            if Text[i] == l:
                pr1 = Profile[l][i]
        pr*=pr1
    return pr
    
def ProfileMostProbableKmer(Text, k, profile):    
    prob = {}
    ans = ""
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        prob[Pattern] = 0
        
    for j in prob.keys():
        prob[j]=Pr(j, profile)
        
    b = max(prob.values())
    
    for p, q in prob.items():
        if q == b:
            ans = p
            break
    return ans
    

Text = "AAGTTC"
Profile = {"A": [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],

"C": [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],

"G": [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],

"T": [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]}
a = Pr(Text, Profile)
print(a)