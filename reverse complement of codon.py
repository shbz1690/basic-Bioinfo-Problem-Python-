# reverse complement of codon

import sys
input_codon=sys.argv[1]

def complement1(nuc):
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

def complement2(nuc):
    nt='ATGC'
    compl='TACG'
    i=nt.find(nuc)
    if i>=0:
        comp=compl[i]
    else:
        comp=nuc
    return comp


def complement3(nuc):
    nt='ATGCatgc'
    compl='TACGtacg'
    i=nt.find(nuc)
    if i>=0:
        comp=compl[i]
    else:
        comp=nuc
    return comp

    
def rev_comp1(nucl):
    nucl=nucl.upper()
    rev_comp=''
    for i in nucl:
        compl=complement1(i)
        rev_comp = compl+rev_comp
    return rev_comp

def rev_comp2(nucl):
    nucl=nucl.upper()
    rev_comp=''
    for i in nucl:
        compl=complement2(i)
        rev_comp = compl+rev_comp
    return rev_comp

def rev_comp3(nucl):
    rev_comp=''
    for i in nucl:
        compl=complement3(i)
        rev_comp = compl+rev_comp
    return rev_comp

print "reverse complement 1 is:",rev_comp1(input_codon)
print "reverse complement 2 is:",rev_comp2(input_codon)
print "reverse complement 3 is:",rev_comp3(input_codon)
