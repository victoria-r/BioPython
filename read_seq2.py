#!/usr/bin/env python3
# read_seq2.py
from Bio import SeqIO
import re

infile = "/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta"

for record in SeqIO.parse(infile, "fasta"):
    if re.match("^\d{1}\D*$", record.id):
        # Get the number of bases
        num_bases = len(record.seq)
        # Format the output
        print("Chromosome {} has {:,} bases".format(record.id, num_bases))
        # we can do the same with an f-string
        # print(f"Chromosome {record.id} has {num_bases:,} bases")
