class basicfn:
    def __init__(self,seq="",name=""):
            self.seq = seq

    def trans_frame(self):
	start_codon="atg"
	index_start_codon= self.seq.find(start_codon)
	trans_frame= (index_start_codon % 3) +1
	return trans_frame
	
    def gccount(self):
        seq=self.seq.upper()
	a=seq.count('A')
	t=seq.count('T')
	g=seq.count('G')
	c=seq.count('C')
	total_nt=a+t+g+c
	total_aa=total_nt/3
	gc_percent=(float(g+c)/total_nt)*100
	print "GC count in seq is:",
	return round(gc_percent,2)
    
    def rev_seq(self):
        s=[]
        for i in range(1,len(self.seq)+1):
            s.append(self.seq[-i])
        return ''.join(s)


    def comp(self):
        seq1=self.seq.upper()
        co=[]
        for i in seq1:
            if i=='A':
                co.append('T')
            elif i=='T':
                co.append('A')
            elif i=='G':
                co.append('C')
            elif i=='C':
                co.append('G')
            else:
                co.append(i)
        return ''.join(co)

    def rev_comp(self):
        seq2=self.seq.upper()
        k=basicfn(seq2)
        compli=k.comp()
        f=basicfn(compli)
        rev_compl=f.rev_seq()
        return rev_compl
