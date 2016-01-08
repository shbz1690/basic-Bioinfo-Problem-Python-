import sys
from model import *
init()
a=sys.argv[1]

try:
    hs_name = Name.selectBy(name=a)[0]
except:
    print >>sys.stderr, "organism ",a,"does not exist"
    sys.exit(1)


t=hs_name.taxonomy

r=t
sc_name=[]
while r.id != r.parentID:
    sc_name.append(r.scientific_name)
    r=r.parent
print 'scientific name of organism',a,'is :',sc_name[0]
print 'taxonomic lineage for organism',a,'is :'
print 'root',
for i in reversed(sc_name):
    print '<-',i,









