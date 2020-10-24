# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:57:32 2020

@author: Presh
"""

def LinearSpectrum(Peptide, Alphabet, AminoAcidMass):
    PrefixMass = [0]
    for i in range(1, len(Peptide)+1):
        for s in range(0, len(Alphabet)):
           if Peptide[i-1] == Alphabet[s]:
               a = PrefixMass[i-1] + AminoAcidMass[Alphabet[s]]
               PrefixMass.append(a)
    LinearSpectrum = [0]
    for i in range(0, len(Peptide)):
        for j in range(i+1, len(Peptide)+1):
            a = PrefixMass[j] - PrefixMass[i]
            LinearSpectrum.append(a)
    
    return LinearSpectrum

def CyclicSpectrum(Peptide, Alphabet, AminoAcidMass):
    PrefixMass = [0]
    for i in range(1, len(Peptide)+1):
        for s in range(0, len(Alphabet)):
           if Peptide[i-1] == Alphabet[s]:
               a = PrefixMass[i-1] + AminoAcidMass[Alphabet[s]]
               PrefixMass.append(a)
    peptidemass = PrefixMass[len(Peptide)]
    CyclicSpectrum = [0]
    for i in range(0, len(Peptide)):
        for j in range(i+1, len(Peptide)+1):
            a = PrefixMass[j] - PrefixMass[i]
            CyclicSpectrum.append(a)
            if i > 0 and j < len(Peptide):
                b = peptidemass - a
                CyclicSpectrum.append(b)
    return CyclicSpectrum
    
    

#input text file for mass and convert to dict
f = open("integer_mass_table.txt","r")
content = f.read()
content = content.rstrip("\n")
AminoAcidMass = dict((x.strip(), y.strip()) 
             for x, y in (element.split(' ')  
             for element in content.split('\n'))) 
for key,value in AminoAcidMass.items():
    AminoAcidMass[key] = int(AminoAcidMass[key])
Alphabet = list(AminoAcidMass.keys())
Peptide = "AQV"
a = LinearSpectrum(Peptide, Alphabet, AminoAcidMass)
a.sort()
print(a)