import sys
seq_file=sys.argv[1]
seq=''.join(open(seq_file).read().split())


f = open('standard.code')
data = {}
for l in f:
    sl = l.split()
    key = sl[0]
    value = sl[2]
    data[key] = value    
f.close()

b1 = data['Base1']
b2 = data['Base2']
b3 = data['Base3']
aa = data['AAs']
st = data['Starts']

codons = {}
init = {}
n = len(aa)
for i in range(n):
    codon = b1[i] + b2[i] + b3[i]
    codons[codon] = aa[i]
    init[codon] = (st[i] == 'M')
    
sequ='ATCC'
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
        aa1 = codons[codon1]
    else:
        aa1='#'
    aaseq1.append(aa1)
    codon2 = seq[j:j+3]
    if len(codon2)==3:
        aa2 = codons[codon2]
    else:
        aa2='#'
    
    aaseq2.append(aa2)
    codon3 = seq[k:k+3]
    if len(codon3)==3:
        aa3 = codons[codon3]
    else:
        aa3='#'
    aaseq3.append(aa3)

    
    
print 'aa seq from frame shift 1 :'
print ''.join(aaseq1),'\n'
print 'aa seq from frame shift 2 :'
print ''.join(aaseq2),'\n'
print 'aa seq from frame shift 3 :'
print ''.join(aaseq3),'\n'
