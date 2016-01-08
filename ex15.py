from MyDNAStuff import *
from codon_table import *
import sys

table=read_codons_from_filename(sys.argv[1])
seq=read_seq_file(sys.argv[2])
rev_comp=rev_comp(seq)


if len(sys.argv) < 3:
    print "Require codon table and DNA sequence on command-line."
    sys.exit(1)


if is_init(table,seq[:3]):
    print "Initial codon is an initiation codon"


for frame in (1,2,3):
  print "Frame",frame,"(forward):",translate(table,seq,frame)

for frame in (-1,-2,-3):   
  print "Frame",frame,"(reverse):",translate(table,rev_comp,frame)





