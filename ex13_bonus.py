import xml.etree.ElementTree as ET
ns='{http://sashimi.sourceforge.net/schema_revision/mzXML_2.0}'
count1=0
count2=0
count3=0
for event,ele in ET.iterparse("Data1.mzXML"):
    if ele.tag == (ns+'scan'):
        if int(ele.attrib['msLevel'])==1:
            count1=count1+1
        elif int(ele.attrib['msLevel'])==2:
            count2=count2+1
        if float(ele.attrib['lowMz'])>750.0 and float(ele.attrib['lowMz'])< 1000.0:
           count3=count3+1 
    #ele.clear()
print "ms1:",count1
print "ms2:",count2
print "count of m/z: between 750 and 1000 Da: ",count3
