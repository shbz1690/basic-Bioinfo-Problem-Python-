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
d=[]
for r in rows:
    if int(r['TUMOUR']) not in d:
        d.append(int(r['TUMOUR']))

for i in d:
    print i
    for k in rows:
        print 'L'
        if int(k['TUMOUR'])==i:
            print k[gene]
        #summ=summ+float(r[gene])
        #umm1=summ1+int(r[gene])**2
        #count=count+1
        else:
        #d.append(r['TUMOUR'])
            print 'n'
    print 'LL'
print d
file.close()


