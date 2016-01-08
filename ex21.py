import sys
import sqlite3

orgname = sys.argv[1]

conn = sqlite3.connect('taxa.db3')
params = [orgname,'scientific name']
c = conn.cursor()
c.execute("""
   select taxonomy.scientific_name from taxonomy join name on taxonomy.tax_id=name.tax_id
   where name.name = ? and name.name_class = ?;
""",params)
for row in c:
   print row



