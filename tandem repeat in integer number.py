# tandem repeat is in integer number or not

import sys
seq= sys.argv[1]
l=len(seq)
first_nuc=seq[0]
print "DNA sequence consists of an integer number of perfect tandem repeats : ",l%(seq.count(first_nuc))==0
