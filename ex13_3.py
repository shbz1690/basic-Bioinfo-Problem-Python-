import gzip
from xml.dom.minidom import parse, parseString

# open and read gzipped xml file
infile = gzip.open( 'Data1.mzXML.gz' )
content = infile.read()

# parse xml file content
dom = parseString( content )

for i in dom:
    print i
