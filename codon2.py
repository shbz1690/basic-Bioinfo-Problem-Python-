import sys
seq_file=sys.argv[1]
seq1=''.join(open(seq_file).read().split())
seq=seq1.upper()

f = open('standard.code')
data = {}
for l in f:
    sl = l.split()
    key = sl[0]
    value = sl[2]
    data[key] = value    
f.close()

b1 = data['Base1'].upper()
b2 = data['Base2'].upper()
b3 = data['Base3'].upper()
aa = data['AAs'].upper()
st = data['Starts'].upper()

codons = {}
init = {}
n = len(aa)
for i in range(n):
    codon = b1[i] + b2[i] + b3[i]
    codons[codon] = aa[i]
    init[codon] = (st[i] == 'M')
    
aa_dummy1=[]
aa_dummy2=[]
aa_dummy3=[]
seqlen= len(seq)
aaseq1=[]
aaseq2=[]
aaseq3=[]
aa1=''
aa2=''
aa3=''
for i,j,k in zip(range(0,seqlen,3), range(1,seqlen,3), range(2,seqlen,3)):
    codon1 = seq[i:i+3]
    if len(codon1)==3:
        if codon1 in codons:
            aa1 = codons[codon1]
        else:
            if codon1[2] not in 'ATGC':
                for i in 'atgc':
                    codon1= codon1.replace(codon1[2],i)
                    aa_dummy1.append(codons[codon1.upper()])
                if aa_dummy1[0]==aa_dummy1[1]==aa_dummy1[2]==aa_dummy1[3]:
                    aa1=aa_dummy1[0]
                else:
                    aa1='X'
            else:
                aa1='X'
    else:
        aa1='#'
    aaseq1.append(aa1)
    codon2 = seq[j:j+3]
    if len(codon2)==3:
        if codon2 in codons:
            aa2 = codons[codon2]
        else:
            if codon2[2] not in 'ATGC':
                for i in 'atgc':
                    codon2= codon2.replace(codon2[2],i)
                    aa_dummy2.append(codons[codon2.upper()])
                if aa_dummy2[0]==aa_dummy2[1]==aa_dummy2[2]==aa_dummy2[3]:
                    aa2=aa_dummy2[0]
                else:
                    aa2='X'
            else:
                aa2='X'
    else:
        aa2='#'
    aaseq2.append(aa2)
    codon3 = seq[k:k+3]
    if len(codon3)==3:
        if codon3 in codons:
            aa3 = codons[codon3]
        else:
            if codon3[2] not in 'ATGC':
                for i in 'atgc':
                    codon3= codon3.replace(codon3[2],i)
                    aa_dummy3.append(codons[codon3.upper()])
                if aa_dummy3[0]==aa_dummy3[1]==aa_dummy3[2]==aa_dummy3[3]:
                    aa3=aa_dummy3[0]
                else:
                    aa3='X'
            else:
                aa3='X'
    else:
        aa3='#'
    aaseq3.append(aa3)



    
    
print 'aa seq from frame shift 1 :'
print ''.join(aaseq1),'\n'
print 'aa seq from frame shift 2 :'
print ''.join(aaseq2),'\n'
print 'aa seq from frame shift 3 :'
print ''.join(aaseq3),'\n'



