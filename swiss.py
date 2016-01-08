import Bio.SeqIO
import sys
import gzip

# Get the sequence filename
seqfilename = sys.argv[1]

# Open the FASTA file and iterate through its sequences
seqfile = gzip.open(seqfilename)
for seq_record in Bio.SeqIO.parse(seqfile, "swiss"):
    # Print out the various elements of the SeqRecord
    print "\n------NEW SEQRECORD------\n"
    print "seq_record.id:\n\t", seq_record.id
    print "seq_record.description:\n\t",seq_record.description
    print "seq_record.seq:\n\t",seq_record.seq
seqfile.close()
