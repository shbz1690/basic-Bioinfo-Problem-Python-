from Model import *
import sys
a=sys.argv[1]

try:
    hsname = Name.selectBy(name=a)[0]
except IndexError:
    print "Can't find name: ",a
    sys.exit(1)
hs1 = hsname.taxa
print hs1.scientificName



