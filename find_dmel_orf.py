#!/usr/bin/env python3
# find_dmel_orf.py
from Bio.Seq import Seq
from Bio import SeqIO
import re

infile = "/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta"

# Read the Drosophila genome - only full chromosomes
for record in SeqIO.parse(infile, "fasta"):
    if re.match("^\d{1}\D*$", record.id):
       

        # Transcribe the DNA to RNA
        dna = record.seq
        rna = dna.transcribe()
    
        # Find the first ORF in the chromosome
        orf = re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)', str(rna)).group()
        rna_orf = Seq(orf)

        # Translate the ORF to protein
        protein = rna_orf.translate()

        # Print the protein
        print(protein)




