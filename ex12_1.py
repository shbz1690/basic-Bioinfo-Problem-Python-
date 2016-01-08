import Bio.PDB.PDBParser
import sys

parser = Bio.PDB.PDBParser(QUIET=True)
structure = parser.get_structure("1HPV","1HPV.pdb")

achain = structure[0]['A']
bchain = structure[0]['B']

bchainca = [ r['CA'] for r in bchain ]
neighbors = Bio.PDB.NeighborSearch(bchainca)

for res1 in achain:
    a= res1.get_resname()
    if a=='LYS':
        r1ca = res1['CA']
        r1ind = res1.get_id()[1]
        r1sym = res1.get_resname()
        for r2ca in neighbors.search(r1ca.get_coord(), 11.0):
            res2 = r2ca.get_parent()
            b= res2.get_resname()
            if b=='LYS':
                r2ind = res2.get_id()[1]
                r2sym = res2.get_resname()
                print 'distance between',
                print r1sym,r1ind,"in chain A",
                print "and",
                print r2sym,r2ind,"in chain B",
                print 'is',
                print round(r1ca-r2ca,2)
