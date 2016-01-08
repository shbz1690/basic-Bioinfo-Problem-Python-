import xml.etree.ElementTree as ET

document = ET.parse("Data1.mzXML")
root = document.getroot()
count1=0
count2=0
for e in root.getiterator('scan'):
    print "y"
    if e.attrib['msLevel']==1:
        count1=count1+1
    elif e.attrib['msLevel']==2:
        count2=count2+1
    
print "MS spectra with msLevel1 :", count1
print "MS spectra with msLevel2 :", count2
    

        
