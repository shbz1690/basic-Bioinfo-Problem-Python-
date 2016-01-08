from codon_table import *
import sys
seq_file=sys.argv[1]
codon_file=sys.argv[2]
print translate(codon_file,seq_file,1)

    
    
