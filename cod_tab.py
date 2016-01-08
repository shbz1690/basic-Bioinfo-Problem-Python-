def read_codons_from_filename(codonfile):
    f=open(codonfile)
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

    codon_table = {}
    n = len(aa)
    for i in range(n):
        codon = b1[i] + b2[i] + b3[i]
        isInit = (st[i] == 'M')
        codon_table[codon] = (aa[i],isInit)
    return codon_table

def amino_acid(table,codon):
    codon=codon.upper()
    aa=table[codon][0]
    return aa

def is_init(table,codon):
    init=table[codon][1]
    return init

def get_ambig_aa(table,codon):
    aa_dummy1=[]
    if codon[2] not in 'ATGC':
        for i in 'atgc':
            codon= codon.replace(codon[2],i)
            aa=amino_acid(table,codon)
            aa_dummy1.append(aa)
        if aa_dummy1[0]==aa_dummy1[1]==aa_dummy1[2]==aa_dummy1[3]:
                return aa_dummy1[0]
        else:
            return 'X'
    else:
        return 'X'

def read_seq_file(seq_file):
    seq=''.join(open(seq_file).read().split())
    return seq.upper()

def translate(table,seq,frame):
    seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
    frame=int(frame)
    seq=seq.upper()
    aa_seq=[]
    if frame<0:
        frame=-frame
    for i in range(frame-1,len(seq),3):
        c=seq[i:i+3]
        try:
            if len(c)==3:
                if (c[0] not in 'ATGC') or (c[1] not in 'ATGC') or (c[2] not in 'ATGC'):
                    amino_a=get_ambig_aa(table,c)
                    aa_seq.append(amino_a)
                else:
                    a=amino_acid(table,c)
                    aa_seq.append(a)
                
        except IndexError:
            break
            #for i in range(0,len(c)):
                #aa_seq.append('#')
    aa=''.join(aa_seq)
    return aa








