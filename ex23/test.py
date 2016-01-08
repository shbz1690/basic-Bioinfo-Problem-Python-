# Set up data-model
from Model import *
import sys

organism=sys.argv[1]
hsname = Name.selectBy(name=organism)[0]
hs3 = hsname.taxa

print 'scientfic name of organism',organism,'is :',hs3.scientificName


