import Bio.SeqIO
import sys
import gzip
count = {}
count2={}
if len(sys.argv) < 2:
    print >>sys.stderr, "Please provide a sequence file"
    sys.exit(1)

seqfilename = sys.argv[1]
seqfilename2 = sys.argv[2]

seqfile = gzip.open(seqfilename)
seqfile2 = gzip.open(seqfilename2)
for seq_record in Bio.SeqIO.parse(seqfile, "fasta"):
    aa=seq_record.seq
    for i in aa:
      if count.has_key(i):
        count[i] += 1
      else:
        count[i] = 1

    print seq_record.id
    maxi= max(count, key=count.get)
    mini=min(count, key=count.get)
    print maxi,":",count[maxi], "\t",mini,":",count[mini]
    count.clear()

for seq_record in Bio.SeqIO.parse(seqfile2, "swiss"):
    aa=seq_record.seq
    for i in aa:
      if count2.has_key(i):
        count2[i] += 1
      else:
        count2[i] = 1

    print seq_record.id
    maxi= max(count2, key=count2.get)
    mini=min(count2, key=count2.get)
    print maxi,":",count2[maxi], "\t",mini,":",count2[mini]
    count2.clear()
seqfile.close()



