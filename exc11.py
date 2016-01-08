import Bio.SeqIO
import sys
import gzip

seqfilename = sys.argv[1]
seqfilename2 = sys.argv[2]

print "Enter RefSeq id:",
refseq_id = raw_input()
print "Enter Uniprot id:",
sprot_id=raw_input()
count = {}
count2={}
maxi1=''
mini1=''
maxi2=''
mini2=''

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

    
        maxi1= max(count, key=count.get)
        mini1=min(count, key=count.get)
        print maxi1,":",count[maxi1], "\t",mini1,":",count[mini1]
        break
seqfile.close()
print "Uniprot/SwissProt id: ",sprot_id
seqfile2 = gzip.open(seqfilename2)
for seq_record in Bio.SeqIO.parse(seqfile2, "swiss"):
    aa=seq_record.seq
    l=seq_record.id
    if sprot_id in l:
        for i in aa:
            if count2.has_key(i):
                count2[i] += 1
            else:
                count2[i] = 1
        maxi2= max(count2, key=count2.get)
        mini2=min(count2, key=count2.get)
        print maxi2,":",count2[maxi2], "\t",mini2,":",count2[mini2]    
        break 
seqfile2.close()

if maxi1==maxi2 and mini1==mini2 and count[maxi1]==count2[maxi2] and count[mini1]==count[mini2]:
    print "amino acid freq is same in RefSeq and SwissProt databases"
else:
    print "aa frequency is different in RefSeq and SwissProt database "
    







