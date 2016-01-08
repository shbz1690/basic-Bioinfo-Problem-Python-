import csv
import sys
name=sys.argv[1]
gene=sys.argv[2]
file = open(name)
#rows=csv.DictReader(file,dialect='excel-tab')
rows=csv.DictReader(file)
summ=0.0
summ1=0.0
count=0
for r in rows:
    #print r[gene]
    summ=summ+int(r[gene])
    summ1=summ1+int(r[gene])**2
    count=count+1
print "Mean value for gene",gene,"is: ",(summ/count)
print "Standard Deviation for gene",gene,"is: ",(summ1/count)**1/2
print count
print summ
file.close()
