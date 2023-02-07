#!/usr/bin/env python3
# read_seq.py
from Bio import SeqIO
import re

infile = "/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta"

for record in SeqIO.parse(infile, "fasta"):
    if re.match("^\d{1}\D*$", record.id):
        print(record.id)
