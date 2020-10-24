# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:43:40 2020

@author: Presh
"""

# first, import the random package
import random
# Input:  A dictionary Probabilities whose keys are k-mers and whose values are the probabilities of these kmers
# Output: A randomly chosen k-mer with respect to the values in Probabilities



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

#in comments, worked for test cases
def WeightedDie1(Probabilities):
    n = random.uniform(0, 1)
    for p in Probabilities:
        n -= Probabilities[p]
        if n <= 0:
            return p

input = {'AC': 0.1, 'GC': 0.2, 'TA': 0.4, 'CA': 0.1, 'GT': 0.2}
a = WeightedDie(input)
print(a)