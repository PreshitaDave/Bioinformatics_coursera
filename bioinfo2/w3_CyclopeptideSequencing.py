# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 17:25:49 2020

@author: Presh
"""
def Expand(CandidatePeptides):
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
    
    
    

def CyclopeptideSequencing(Spectrum):
    CandidatePeptides = [""]
    FinalPeptides = []
    while CandidatePeptides != 0:
        CandidatePeptides = Expand(CandidatePeptides)
        for Peptide in CandidatePeptides:
            if Mass(Peptide) == ParentMass(Spectrum):
                if Cyclospectrum(Peptide) == Spectrum and Peptide is not in ﻿FinalPeptides:
                    FinalPeptides.append(Peptide)
                    CandidatePeptides.remove(Peptides)
                elif Peptide not in Spectrum:
                    CandidatePeptides.remove(Peptides)
    return FinalPeptides
                
Spectrum = [0, 113, 128, 186, 241, 299, 314, 427]
a = CyclopeptideSequencing(Spectrum)
print(a)
    