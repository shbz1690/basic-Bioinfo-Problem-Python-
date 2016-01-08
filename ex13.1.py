import xml.etree.ElementTree as ET
import urllib
import sys
idd=sys.argv[1]
thefile = urllib.urlopen('http://www.uniprot.org/uniprot/'+idd+'.xml')
document = ET.parse(thefile)
root = document.getroot()
TITLE=0
ns = '{http://uniprot.org/uniprot}'
count=1
for child in root.getiterator(ns+'citation'):
     author=[]
     for k in child.getiterator(ns+'person'):
          author.append(k.get('name'))
     print "REFERENCE: ", count
     print "TITLE: ",child[TITLE].text
     print "CITATION: ",child.attrib
     print "AUTHOR :"
     print ', '.join(author)
     print '\n'
     count=count+1




     
     
    
    
    



        








