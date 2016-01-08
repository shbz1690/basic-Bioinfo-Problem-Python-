class codon_tableclass:
        
    def read_codons_from_filename(self,codonfile):
        self.f=open(codonfile)
        data = {}
        for l in self.f:
            sl = l.split()
            key = sl[0]
            value = sl[2]
            data[key] = value    
        self.f.close()

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

    def amino_acid(self,table,codon):
        codon=codon.upper()
        aa=table[codon][0]
        return aa

    def is_init(self,table,codon):
        init=table[codon][1]
        return init

    def get_ambig_aa(self,table,codon):
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

    def read_seq_file(self,seq_file):
        self.seq=''.join(open(seq_file).read().split())
        return self.seq.upper()

    def translate(self,table,seq,frame):
        seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
        frame=int(frame)
        seq=seq.upper()
        aa_seq=[]
        if frame<0:
            frame=-frame
        for i in range(frame-1,len(seq),3):
            c=seq[i:i+3]
            if len(c)==3:
                if (c[0] not in 'ATGC') or (c[1] not in 'ATGC') or (c[2] not in 'ATGC'):
                    amino_a=codon_tableclass().get_ambig_aa(table,c)
                    aa_seq.append(amino_a)
                else:
                    a=codon_tableclass().amino_acid(table,c)
                    aa_seq.append(a)
                
        #else:
         #   for i in range(0,len(c)):
          #      aa_seq.append('#')
        aa=''.join(aa_seq)
        return aa









