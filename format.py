#!/usr/bin/env python3
# format.py
num_bases = 50000
chrom = '2L'
gene_name = 'XYZ'

# Create the template
template = "Chromosome {} has {:,} bases. Put another variable here {}"

# Print the formatted output
print(template.format(chrom, num_bases, gene_name))
# with f-string
print(f'Chromosome {chrom} has {num_bases:,} bases. Put another variable here {gene_name}')
