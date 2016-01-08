import sys
from model import *
init()
organism = sys.argv[1]

name = Name.selectBy(name=organism)[0]
#print name
taxonomyID = name.taxonomyID
#print taxonomyID
taxonomy = Taxonomy.selectBy(id=taxonomyID)[0]
#print taxonomy

t = taxonomy
#print t

#print t.scientific_name

while t.id != t.parentID:
    #print t.scientific_name,
    t=t.parent
    


