# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:10:33 2020

@author: Presh
"""

# Input: A dictionary Probabilities, where keys are k-mers and values are the probabilities of these k-mers (which do not necessarily sum up to 1)
# Output: A normalized dictionary where the probability of each k-mer was divided by the sum of all k-mers' probabilities
def Normalize(Probabilities):
    # your code here
    sum = 0
    for i, j in Probabilities.items():
        sum += Probabilities[i]
    for i, j in Probabilities.items():
        Probabilities[i] /= sum 
    return Probabilities

input = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}
a = Normalize(input)
print(a)