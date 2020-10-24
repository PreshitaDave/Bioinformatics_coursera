# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:22:22 2020

@author: Presh
"""

# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)


def Motifs(Profile, Dna):
    # insert your code here
    mot = []
    k = 4
    for i in range(0, len(Dna)): 
        b = ProfileMostProbableKmer(Dna[i], k, Profile)
        mot.append(b)
    return mot

# Insert your ProfileMostProbablePattern(Text, k, Profile) and Pr(Pattern, Profile) functions here.
        
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
    
Profile= { 'A': [2, 1, ],'C': [], 'G': [], 'T': []}  
Dna=["ATGAGGTC",
     "GCCCTAGA",
     "AAATAGAT",
     "TTGTGCTA"]
k = len(Dna[0])
t = 5
a = Motifs(Profile, Dna)
print(a)
