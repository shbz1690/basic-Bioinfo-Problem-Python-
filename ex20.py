from Bio.Blast import NCBIXML

result_handle = open("results.xml")
for blast_result in NCBIXML.parse(result_handle):
    a=[]
    print '*******'
    print blast_result.query
    print '*******'
    for desc in blast_result.descriptions:
        #a={desc.title:desc.e}
        #print desc.title
        a.append(desc.e)
        #b.append(desc.title)
    #if len(a)>0:
        #print min(a)
    #print a['gnl|BL_ORD_ID|109 gi|6320119|ref|NP_010199.1| Sub2p [Saccharomyces cerevisiae S288c]']
