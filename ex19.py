from Bio import Entrez
import os.path
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

Entrez.email = 'msk90@georgetown.edu'

handle = Entrez.esearch(db="protein",
         term="Homo sapiens[Organism] AND LIME1[Gene Name] AND REFSEQ")
result = Entrez.read(handle)
print 'Entrez Id list:',result["IdList"],'\n'

for idd in result["IdList"]:
    print "blastp-refseq_protein-"+idd+".xml"
    if not os.path.exists("blastp-refseq_protein-"+idd+".xml"):
        result_handle = NCBIWWW.qblast("blastp", "refseq_protein", idd)
        blast_results = result_handle.read()
        result_handle.close()

        save_file = open("blastp-refseq_protein-"+idd+".xml", "w")
        save_file.write(blast_results)
        save_file.close()


    result_handle = open("blastp-refseq_protein-"+idd+".xml")
    for blast_result in NCBIXML.parse(result_handle):
        for desc in blast_result.descriptions:
            a=desc.title.find('[Mus musculus]')
            if a>0:
                if desc.e < 1e-5:
                    print '****Alignment****'
                    print 'title:', desc.title
                    print 'e value:', desc.e,'\n'
            
                








