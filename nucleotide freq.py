import sys
seq=sys.argv[1]
count = {}
for i in seq:
  if count.has_key(i):
    count[i] += 1
  else:
    count[i] = 1

for i in sorted(count, key=count.get, reverse=True):
  print i, count[i]
