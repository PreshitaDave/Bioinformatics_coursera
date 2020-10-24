# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 20:01:39 2020

@author: Presh
"""

def dnatorna(Text):
    Text = Text.replace("T","U")
    return Text

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

def Translation(pattern, geneticcode, j):
    prt = ""
    n = len(pattern)
    for i in range(j,n+1,3):
        for key,value in geneticcode.items():
            if pattern[i:i+3] == key:
                if value != "STOP":
                    prt += value
                else:
                    prt += '*'
                
    return prt


def peptideencode(Text, peptide, geneticcode):
    substr_pos = []
    substr = []
    rf = []
    #convert text to rna
    str1 = dnatorna(Text)
    rev_str = ReverseComplement(Text)
    rev_str1 = dnatorna(rev_str)
    
    # all 6 reading frames
    str1_0 = Translation(str1, geneticcode, 0)
    str1_1 = Translation(str1, geneticcode, 1) 
    str1_2 = Translation(str1, geneticcode, 2)
    rev1_0 = Translation(rev_str1, geneticcode, 0)
    rev1_1 = Translation(rev_str1, geneticcode, 1)
    rev1_2 = Translation(rev_str1, geneticcode, 2)
    rf = [str1_0,str1_1,str1_2,rev1_0,rev1_1,rev1_2]
    n = len(rf)

    
    for k in range(0,n):
        c = len(rf[k])
        for i in range(0,c+1,len(peptide)):
            if rf[k][i:i+2] == "MA":
                substr_pos.append(i)
                if k==0: 
                    substr.append(Text[i*3:(i*3)+6]) 
                elif k==1:
                    substr.append(Text[(i+1)*3:((i+1)*3)+6])
                elif k==2:
                    substr.append(Text[(i+2)*3:((i+2)*3)+6])
                elif k==3:
                    q = (rev_str[i*3:(i*3)+6])
                    substr.append(q)
                elif k==4:
                    q = (rev_str[(i+1)*3:((i+1)*3)+6])
                    substr.append(q)
                else:
                    q = (rev_str[(i+2)*3:((i+2)*3)+6])
                    substr.append(q)
    return substr
    

Text = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
peptide = "MA"
geneticcode = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
a = peptideencode(Text, peptide, geneticcode)
print(a)