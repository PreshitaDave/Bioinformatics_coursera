# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        # add each key to words whose corresponding frequency value is equal to m
        if freq[key] == m:
            words.append(key)
    return words


#generate a frequency map from a given string and integer
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    # hint: your code goes here!
    for j in freq.keys():
        count = 0
        for i in range(len(Text)-len(Pattern)+1):
            if Text[i:i+len(Pattern)] == j:
                count = count+1
        freq[j]=count
        
    return freq

Text = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
k=3
b = FrequentWords(Text, k)
print(b)

