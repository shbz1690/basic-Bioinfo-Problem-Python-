import sys
seq=sys.argv[1]
seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
print "reverse complement is:"
print "".join(seq_dict[i] for i in reversed(seq.upper().strip()))
