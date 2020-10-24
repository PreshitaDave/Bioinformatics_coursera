# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 18:39:25 2020

@author: Presh
"""
def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

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
    count = CountWithPseudocounts(Motifs)
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

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {} # output variable
    # your code here
    profile = CountWithPseudocounts(Motifs)
    for i in profile.keys():  
        for j in range(k):
            profile[i][j] = profile[i][j]/(t+4)      
    return profile

# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    # insert your code here
    count = {} # initializing the count dictionary
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(1)
             
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
             
    return count

    
    
    
Dna = ["GGCGTTCAGGCA",
"AAGAATCAGTCA",
"CAAGGAGTTCGC",
"CACGTCAATCAC",
"CAATAATATTCG"]
k = 3
t = 5
a = GreedyMotifSearchWithPseudocounts(Dna, k, t)
print(a)