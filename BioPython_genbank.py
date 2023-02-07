#!/usr/bin/env python3
# BioPython_genbank.py
"""BioPython script that prints out objects retrived from GenBank"""

# Set email
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "liebsch.v@northestern.edu"

# Make list with Seq objects
seq_list = ["515056", "J01673.1"]

# Fetch sequences and use Seq.IO parse for multiple records 
handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id=seq_list)
for seq_records in SeqIO.parse(handle, "gb"):

    # Print sequences, type, location, strand
    print(seq_records.id, '\n', seq_records.seq, '\n', seq_records.features)

# Close file
handle.close()
