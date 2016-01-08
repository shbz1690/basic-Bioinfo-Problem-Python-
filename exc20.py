from Bio.Blast import NCBIXML

result_handle = open("results.xml")
evalue=[]
rtitle=[]
query=[]
score_list=[]
for blast_result in NCBIXML.parse(result_handle):
    a=[]
    b=[]
    for desc in blast_result.descriptions:
        if desc.e < 1e-5:
            a.append(desc.e)
            b.append(desc.title)
            evalue.append(desc.e)
            rtitle.append(desc.title)
            query.append(blast_result.query)
            score_list.append(desc.score)
    if len(b)>0:
        print 'Query: ',blast_result.query
        print 'Result :',b[0]
    if len(a)>0:
        print 'e-value :',min(a)
        print 
    del a[:]
    del b[:]
mini=evalue.index(min(evalue))
print '\nhighly conserved ribosomal protein :'
print 'query :',query[mini]
print 'result :',rtitle[mini]
print 'e-value :',evalue[mini]
print 'score :',score_list[mini]
print
    
    
    
        
    
