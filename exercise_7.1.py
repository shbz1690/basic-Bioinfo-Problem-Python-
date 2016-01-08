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

    
def rev_comp1(nuc):
    nucl1=nuc.upper()
    rev_comp1=''
    rev_comp2=''
    rev_comp3=''
    for i in nucl1:
        compl1=complement1(i)
        compl2=complement2(i)
        rev_comp1 = compl1+rev_comp1
        rev_comp2 = compl2+rev_comp2
    for i in nuc:
        compl=complement3(i)
        rev_comp3 = compl+rev_comp3
    return rev_comp1,rev_comp2,rev_comp3


rc=rev_comp1(input_codon)
print "reverse complement of",input_codon," is :",'\n',rc[0],'\n',rc[1],'\n',rc[2]

