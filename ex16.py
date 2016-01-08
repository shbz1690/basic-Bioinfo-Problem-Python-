from MyDNA import *
from cod_tab import *
import sys
seq_file=sys.argv[1]

seq=''.join(open(seq_file).read().split())

print "reverse seq is:",rev_seq(seq)
print "translation frame is:",trans_frame(seq)
print gccount(seq)
print "complement is:",comp(seq)
print "rev comp is:",rev_comp(seq)
    
    
















