class MyDNAStuffClass:

    #def __init__(self,seq):
        #self.seq = seq
    
    def rev_seq(self,seq):
        s=[]
        for i in range(1,len(seq)+1):
            s.append(seq[-i])
        return ''.join(s)
        
        

    def trans_frame(self,seq):
            start_codon="atg"
            index_start_codon= self.seq.find(start_codon)
            trans_frame= (index_start_codon % 3) +1
            return trans_frame
	
    def gccount(self,seq):
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

    def comp(self,seq):
        co=[]
        for i in seq:
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

    def rev_comp(self,seq):
        compliment=MyDNAStuffClass().comp(seq)
        rev_compliment=MyDNAStuffClass().rev_seq(compliment)
        return rev_compliment
    


