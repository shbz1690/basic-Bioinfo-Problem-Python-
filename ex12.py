import Bio.PDB.PDBParser
import sys

parser = Bio.PDB.PDBParser(QUIET=True)
structure = parser.get_structure("1HPV","1HPV.pdb")

achain = structure[0]['A']
bchain = structure[0]['B']

for res1 in achain:
    a= res1.get_resname()
    if a=='LYS':
        if res1.get_id()[0][0] is 'H' or res1.get_id()[0][0] is 'W':
            continue
        r1ca = res1['CA']
        r1ind = res1.get_id()[1]
        r1sym = res1.get_resname()
        
        for res2 in bchain:
            b= res2.get_resname()
            if b=='LYS':
                if res2.get_id()[0][0] is 'H' or res2.get_id()[0][0] is 'W':
                    continue
                r2ca = res2['CA']
                r2ind = res2.get_id()[1]
                r2sym = res2.get_resname()
                if (r1ca - r2ca) > 10.0 and (r1ca - r2ca) < 12.0:
                    print "Residues",r1sym,r1ind,"in chain A",
                    print "and",r2sym,r2ind,"in chain B",
                    print "are close to each other:",round(r1ca-r2ca,2)
                
                


