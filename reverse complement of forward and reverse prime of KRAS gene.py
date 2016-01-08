# reverse complement of forward and reverse prime of KRAS gene

import sys
fwd_primer=sys.argv[1]
rev_primer=sys.argv[2]

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

print "reverse complement of forward primer of KRAS gene is:",rev_comp(fwd_primer)
print "reverse complement of reverse primer of KRAS gene is:",rev_comp(rev_primer)
    
