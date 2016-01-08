import sys
input_seq = sys.argv[1]

first_nuc=input_seq[0]
l=len(input_seq)
half=(l/2)
if input_seq.count(first_nuc)== l:
    print "DNA sequence consists integer number of repeats"
elif l%2==0:
    if input_seq[0:half]==input_seq[half+1:-1]:
        print "DNA sequence consists integer number of repeats"
        
    
