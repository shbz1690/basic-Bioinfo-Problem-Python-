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


seqlen= len(seq)
aaseq=[]
for i in range(0,seqlen,3):
    codon = seq[i:i+3]
    aa = codons[codon]
    aaseq.append(aa)
    
print "initial codon is start codon and valid translational site in sasp bacterium",init[seq[0:3]]
print ''.join(aaseq)
