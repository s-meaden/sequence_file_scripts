#!/usr/bin/env python3

# Script to find every occurence of GG in a genome.
# Then print the subsequent 32bp. 

import re # regular expression module
from Bio import SeqIO # sequence data module
import sys
import regex as re

filename = sys.argv[1] # name of input file i.e. DMS3.fasta
outfile = sys.argv[2] # name of output i.e. spacers.fna

# Find PAM sites, select subsequent 32bp and write out:

with open(outfile,"w") as f:
	for record in SeqIO.parse(filename, "fasta"):
		for match in re.finditer('GG', str(record.seq), overlapped=True): # get iterator to print end of PAM
			spacer_start = match.end() # Location of end of PAM
			spacer_end = spacer_start + 32 # Can vary for spacer length 
			f.write(">" + str(spacer_start) + "\n" + str(record.seq)[spacer_start:spacer_end] + "\n") # Write out as fasta file








