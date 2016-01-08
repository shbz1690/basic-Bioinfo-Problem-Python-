import csv
import sys
name=sys.argv[1]
gene=sys.argv[2]
file = open(name)
rows=csv.DictReader(file)
summ1=0.0
summ2=0.0
square1=0.0
square2=0.0
count1=0
count2=0

for r in rows:
    if int(r['TUMOUR'])==1:
        summ1=summ1+float(r[gene])
        square1=square1+(float(r[gene]))**2
        count1=count1+1
    else:
        summ2=summ2+float(r[gene])
        square2=square2+(float(r[gene]))**2
        count2=count2+1

variance1=square1/count1
variance2=square2/count2
print "For Sample_1 and gene",gene,":"
print "Mean:",summ1/count1
print "Standard Deviation: ",(variance1)**1/2
print "For Sample_2 and gene",gene,":"
print "Mean: ",summ2/count2
print "Standard Deviation: ",(variance2)**1/2
      
file.close()


