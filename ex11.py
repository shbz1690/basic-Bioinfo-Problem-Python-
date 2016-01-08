import Bio.SeqIO
import sys
import gzip

seqfilename = sys.argv[1]
seqfilename2 = sys.argv[2]

refseq_id=sys.argv[3]
sprot_id=sys.argv[4]
count = {}
count2={}

if len(sys.argv) < 2:
    print >>sys.stderr, "Please provide a sequence file"
    sys.exit(1)


print "RefSeq id: ",refseq_id

seqfile = gzip.open(seqfilename)
for seq_record in Bio.SeqIO.parse(seqfile, "fasta"):
    aa=seq_record.seq
    idd= seq_record.id.split('|')
    if refseq_id==idd[3]:
        for i in aa: 
          if count.has_key(i):
            count[i] += 1
          else:
            count[i] = 1

    
        maxi= max(count, key=count.get)
        mini=min(count, key=count.get)
        print maxi,":",count[maxi], "\t",mini,":",count[mini]
    count.clear()
seqfile.close()

print "Uniprot id: ",sprot_id
seqfile2 = gzip.open(seqfilename2)
for seq_record in Bio.SeqIO.parse(seqfile2, "swiss"):
    aa=seq_record.seq
    if sprot_id==seq_record.id:
        for i in aa:
            if count2.has_key(i):
                count2[i] += 1
            else:
                count2[i] = 1
        maxi= max(count2, key=count2.get)
        mini=min(count2, key=count2.get)
        print maxi,":",count2[maxi], "\t",mini,":",count2[mini]    
         
    count2.clear()
seqfile2.close()
    
    

# Open the FASTA file and iterate through its sequences







