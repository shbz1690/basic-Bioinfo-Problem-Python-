# Reverse complement is a pallindrome of input DNA sequence or not.

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

def rev_comp(nucl):
    nucl=nucl.upper()
    rev_comp=''
    for i in nucl:
        compl=comp(i)
        rev_comp = compl+rev_comp
    return rev_comp

rev_complement=rev_comp(input_codon)
print "reverse complement is a pallindrome of original sequence :",rev_complement==input_codon
    
