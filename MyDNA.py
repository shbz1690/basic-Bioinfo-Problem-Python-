def rev_seq(seq):
    s=[]
    try:
        len(seq)/len(seq)
        for i in range(1,len(seq)+1):
            s.append(seq[-i])
        return ''.join(s)
    except ZeroDivisionError:
            return "Error: no sequence entered"        

def trans_frame(seq):
	start_codon="atg"	
	index_start_codon= seq.find(start_codon)
	try:
            index_start_codon/(index_start_codon+1)
            trans_frame= (index_start_codon % 3) +1
            return trans_frame
        except ZeroDivisionError:
            return "Error: no initiation codon found in sequence"
	
def gccount(seq):
    try:
        len(seq)/len(seq)
        seq=seq.upper()
	a=seq.count('A')
	t=seq.count('T')
	g=seq.count('G')
	c=seq.count('C')
	total_nt=a+t+g+c
	try:
            total_aa=total_nt/3
            gc_percent=(float(g+c)/total_nt)*100
            print "GC count in seq is:",
            return round(gc_percent,2)
        except ZeroDivisionError:
            return "Error: no ATGC nucleotide found in file"
    except ZeroDivisionError:
            return "Error: no sequence entered"
            


def comp(seq):
    try:
        len(seq)/len(seq)
        seq=seq.upper()
        compl_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
        compl=''
        for i in seq:
            try:
                compl=compl+compl_dict[i]
            except KeyError:
                compl=compl+i
        return compl
    except ZeroDivisionError:
            return "Error: no sequence entered" 
        

def rev_comp(seq):
    try:
        len(seq)/len(seq)
        compliment=comp(seq)
        rev_compliment=rev_seq(compliment)
        return rev_compliment
    except ZeroDivisionError:
            return "Error: no sequence entered"
    

