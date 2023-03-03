# BioPython 

## create_seq.py

Creates the fasta file ```kmers.fasta```.

## find_dmel_orf.py

Finds the first open reading frame (ORF) from the non-local fasta file ```/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta```. Translates the OFT to protein and prints out the protein.

## find_orf.py

Finds the ORF from a DNA sequence.

## format.py

Creates a template to print out an organized message.

## read_seq.py

Takes a non-local fasta file and prints out the record id.

## readseq2.py

Uses the template from ```format.py``` and prints out an organized message about a non-local fatsa file.

## transcribe.py

Transcribes a line of random DNA and prints out the RNA.

## translate.py

Prints out a protein sequence that has been translated from transcribed RNA.

## BioPython_seq.py

This BioPython script creates a SeqRecord object with the following parameters:
seq: "aaaatgggggggggggccccgtt"
id: "#12345"
description: "example 1"
alphabet: "generic_dna"
Then the object is written to a sequence file in GenBank format and called BioPyhon_seq.gb.

## BioPython_genbank.py

This BioPython script creates a list with the following Seq objects:
A sequence retrieved from GenBank by gi (id) for 515056
A sequence retrieved from GenBank by accession (id) for J01673.1
Then it prints out the sequences from the list as well as the type, location, and strand of each feature. 

## BioPython_seqio.py

This BioPython script reads a multi-sequence FASTA file and outputs a FASTA file whose contents are the reverse complements of the sequences from the original FASTA file.This script takes two arguments from the command line: the name of the original multi-sequence FASTA file, and the desired name of the new multi-sequence FASTA file. Tested on yeast.fasta. Writes the output yeast_reverse.fasta.

## sliding_window_fasta.py

This BioPython script revises the sliding_window_fasta.py script from SlidingWindow repo to open with SeqIO. This file modifies the script sliding_window.py and uses the same functions but, instead of taking a k-mer size and a string, it takes a k_mer size and a fasta file. It also will run separately for each header, printing the header name on one line, and then each k-mer from that fasta entry followed by a tab, followed by the GC content of that k-mer, rounded to two decimal places. Tested with the dengue.fasta file.

## Getting Started

### Dependencies

* Python3
* A fasta file of choice - used a nonlocal file (not attached), dengue.fasta, and yeast.fasta
* Can download dengue.fasta here: wget -O dengue.fasta 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=NC_001477.1&rettype=fasta' (Links to an external site.)

## Author

Victoria R. Liebsch-Aljawahiri

## Date Created

11 October 2021
