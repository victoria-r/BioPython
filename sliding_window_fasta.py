#!/usr/bin/env python3
# sliding_window_fasta.py
import sys
from Bio import SeqIO

def sliding_window(k, fasta):
    """
    Take 2 arguments: k_mer size and a fasta file
    Returns a list of all k-mers in the fasta file using the sliding window algorithm
    """
    kmers = []
    end = len(fasta) - k + 1
    for start in range(0, end):
        kmers.append(fasta[start:start + k])
    return kmers


def gc_content(dna):
    """
    Takes 1 argument: a single string
    Returns the GC content (as a fraction) of the string
    """
    dna = dna.lower()    # Make the sequence lowercase for consistency
    gc = 0    # Count the number of g's and c's
    for nucleotide in dna:
        if nucleotide in ['g', 'c']:
            gc += 1
    return gc/len(dna)


if __name__ == '__main__':

    # Check to make sure there are at least two arguments
    arg_count = len(sys.argv) - 1
    if arg_count < 2:
        raise Exception("This script requires 2 arguments: kmer size and a fasta file")

    # Get parameters from command line options
    k = int(sys.argv[1])
    fasta = sys.argv[2]
    
    # Reads fatsa with SeqIO, grabs header and sequence to run seperately
    for sequences in SeqIO.parse(fasta, "fasta"):
        print(sequences.id)
    kmer = sequences.seq
 
    # Iterate over function to get each kmer GC content seperately 
    for dna in sliding_window(k, kmer):
        result = gc_content(dna)

        # Print kmer and GC content to 2 decimal places
        print("{}\t{:.2f}".format(dna, result))
