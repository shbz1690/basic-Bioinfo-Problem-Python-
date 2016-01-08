from MyDNAStuffClass import *
from codon_tableclass import *
import sys

c = codon_tableclass()
table= c.read_codons_from_filename(sys.argv[1])
seq=c.read_seq_file(sys.argv[2])

d=basicfn(seq)
rev_comp=d.rev_comp()


if len(sys.argv) < 3:
    print "Require codon table and DNA sequence on command-line."
    sys.exit(1)


if c.is_init(table,seq[:3]):
    print "Initial codon is an initiation codon"


for frame in (1,2,3):
  print "Frame",frame,"(forward):",c.translate(table,seq,frame)

for frame in (-1,-2,-3):   
  print "Frame",frame,"(reverse):",c.translate(table,rev_comp,frame)


