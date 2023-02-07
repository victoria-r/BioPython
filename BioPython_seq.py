#!/usr/bin/env python3
# BioPython_seq.py
"""Creates SeqRecord object and writes it into a GenBank file"""

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
from Bio import SeqIO

# Create SeqRecord object
my_seq = Seq("aaaatgggggggggggccccgtt", generic_dna)
my_seq_r = SeqRecord(my_seq, id="#12345", description="example 1")

# Write object to a sequence file in GenBank format
SeqIO.write(my_seq_r, "BioPython_seq.gb", "gb")
