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
aaseq1=[]
aaseq2=[]
aaseq3=[]
for i in range(k,seqlen,3):
    if k==0:
        codon1 = seq[i:i+3]
        aa1 = codons[codon1]
        aaseq1.append(aa1)
    elif k==1:
        codon2 = seq[i:i+3]          
        aa2 = codons[codon2]
        aaseq2.append(aa2)
    elif k==2:
        codon3 = seq[i:i+3]          
        aa3 = codons[codon3]
        aaseq3.append(aa3)
    
    
print 'translation at frame 1 is : '.join(aaseq1)
print 'translation at frame 1 is : '.join(aaseq2)
print 'translation at frame 1 is : '.join(aaseq3)
