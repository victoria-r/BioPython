#!/usr/bin/env python3
# translate.py
# Import Seq
from Bio.Seq import Seq

dna = Seq("AGTACACTGGTA")
rna = dna.transcribe()
protein = rna.translate()

print(protein)
