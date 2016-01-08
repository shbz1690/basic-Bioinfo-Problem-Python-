# Reverse complement is a pallindome of itself orr not.

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
l=len(rev_complement)
k=-1
rev_rev=''
for i in rev_complement:
    rev_rev=rev_rev+rev_complement[k]
    k=k-1
print "reverse complement is a pallindome of itself",rev_complement==rev_rev
