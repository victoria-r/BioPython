#!/usr/bin/env python3
# BioPython_seqio.py
"""Redas a fasta file and writes the reverse complement of that file"""

import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# Get fatsa file and new fasta name from command line options
original_fasta = sys.argv[1]
new_fasta = sys.argv[2]

# Reads fasta file
for seq_record in SeqIO.parse(original_fasta, "fasta"):

    # Get sequences and reverse complements
    orig_dna = seq_record.seq
    rcomp_dna = orig_dna.reverse_complement()
    
    # Conver Seq object into SeqRecord object for writing
    rcomp_dna_r = SeqRecord(rcomp_dna, id="Reverse complement of yeast.fasta")

    # Write reverse complements to new fasta file
    SeqIO.write(rcomp_dna_r, new_fasta, "fasta")

# Check to mak esure there are atleast two arguments
arg_count = len(sys.argv) - 1
if arg_count < 2:
    raise Exception("This script requires 2 arguments: \
        a fasta file and the desired name of the reverse complement fasta file.")
