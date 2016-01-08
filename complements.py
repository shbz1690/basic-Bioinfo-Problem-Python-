# reverse complement of codon

import sys
input_codon=sys.argv[1]

def comp(nuc):
    if nuc=='A':
        comp='T'
    elif nuc=='T':
        comp='A'
    elif nuc=='G':
        comp='C'
    elif nuc=='C':
        comp='G'
    else:
        comp=nuc
    return comp

def complement1(nuc):    
    nucleotides = 'ACGTatgc'    
    complements = 'TGCAtgca'    
    i = nucleotides.find(nuc)    
    if i >= 0:        
        comp = complements[i]    
    else:        
        comp = nuc    
    return comp

def complement2(nuc):    
    nucleotides = 'ACGTatgc'    
    complements = 'TGCAtgca'    
    i = nucleotides.find(nuc)    
    if i >= 0:        
        comp = complements[i]    
    else:        
        comp = nuc    
    return comp

def rev_comp(nucl):
    nucl=nucl.upper()
    rev_comp=''
    for i in nucl:
        compl=comp(i)
        rev_comp = compl+rev_comp
    return rev_comp

print "reverse complement is:",rev_comp(input_codon)
    
