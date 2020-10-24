# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 19:11:21 2020

@author: Presh
"""

# first, import the random package
import random
# then, copy Pr, Normalize, and WeightedDie below this line
def Normalize(Probabilities):
    # your code here
    sum = 0
    for i, j in Probabilities.items():
        sum += Probabilities[i]
    for i, j in Probabilities.items():
        Probabilities[i] /= sum 
    return Probabilities


def WeightedDie(Probabilities):
    kmer = '' # output variable
    # your code here
    p = random.uniform(0, 1)
    sum = 0
    for i, j in Probabilities.items():
        sum += j
        Probabilities[i] = sum
    for i,j in Probabilities.items():
        if j >= p:
            kmer = i
            break
    return kmer

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


# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    # your code here
    n = len(Text)
    probabilities = {} 
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)
    
Text = "AAACCCAAACCC"
profile = {'A': [0.5, 0.1], 'C': [0.3, 0.2], 'G': [0.2, 0.4], 'T': [0.0, 0.3]}
k = 2
a = ProfileGeneratedString(Text, profile, k)
print(a)