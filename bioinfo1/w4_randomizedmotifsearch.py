# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:52:46 2020

@author: Presh
"""
# first, import the random package
import random
# Next, copy your RandomizedMotifSearch function (along with all required subroutines)
# from Motifs.py below this line


def RandomMotifs(Dna, k, t):
    randmot = []
    l = len(Dna[0])
    for i in range(t):
        r = random.randint(1, l-k)
        r1 = Dna[i][r:r+k]
        randmot.append(r1)
    return randmot


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

def Motifs(Profile, Dna, k):
    # insert your code here
    mot = []
    for i in range(0, len(Dna)): 
        b = ProfileMostProbableKmer(Dna[i], k, Profile)
        mot.append(b)
    return mot

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

# for profilewithpseudocount fn 
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



def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna, k)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs 
    
    

# Copy the ten strings occurring in the hyperlinked DosR dataset below.

Dna=["ATGAGGTC",
     "GCCCTAGA",
     "AAATAGAT",
     "TTGTGCTA"]
t = 4 
k = 3
N = 2
# Call RandomizedMotifSearch(Dna, k, t) N times, storing the best-scoring set of motifs
def RepeatedRandomizedMotifSearch(Dna, k, t):
    BestScore = float('inf')
    BestMotifs = []
    for i in range(N):
        Motifs = RandomizedMotifSearch(Dna, k, t)
        CurrScore = Score(Motifs)
        if CurrScore < BestScore:
            BestScore = CurrScore
            BestMotifs = Motifs
    return BestMotifs

# resulting from this algorithm in a variable called BestMotifs
BestMotifs = RepeatedRandomizedMotifSearch(Dna, k, t)

# Print the BestMotifs variable
print(BestMotifs)
# Print Score(BestMotifs)
print(Score(BestMotifs))