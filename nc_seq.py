
# Import the required modules
import sys

# Check there is user input
if len(sys.argv) < 2:
    print "Please provide a DNA sequence file on the command-line."
    sys.exit(1)

# Assign the user input to a variable
seqfile = sys.argv[1]
# and read the sequence
seq = ''.join(file(seqfile).read().split())

# Compute the sequence length
for nuc in seq:
    if nuc not in 'ACGT':
        

# Output a summary of the user input and the result
print "Input DNA sequence:",seq
print "Input DNA sequence length:",seqlen
