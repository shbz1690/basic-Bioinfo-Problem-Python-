import os.path
from Bio.Blast import NCBIWWW

if not os.path.exists("blastn-nr-8332116.xml"):

    result_handle = NCBIWWW.qblast("blastn", "nr", "8332116")
    blast_results = result_handle.read()
    result_handle.close()

    save_file = open("blastn-nr-8332116.xml", "w")
    save_file.write(blast_results)
    save_file.close()
