import sys
from Bio.Seq import Seq
from Bio.Alphabet import generic_rna
rna_str = sys.stdin.read()


# Using BioPython
def prot(s):
    """ Takes an RNA string s corresponding to a strand of mRNA. Returns the protein string encoded by s. """
    messenger_rna = Seq(s, generic_rna)
    p = messenger_rna.translate(to_stop=True)
    return p

print prot(rna_str)


# Not using BioPython
def prot2(s):
    """ Takes an RNA string s corresponding to a strand of mRNA. Returns the protein string encoded by s. """

    # Make dictionary of rna codons and amino acids
    import re
    codon_file = open("rna_codon_table.txt", "r")
    codon_to_amino_acid_dict = {}
    for line in codon_file:

        # Split by white spaces longer than one
        groupings = re.split(r'\s{2,}', line)

        # Remove new line character at the end of last pair
        groupings[3] = groupings[3][0:5]

        for g in groupings:
            g = g.split()
            codon = g[0]
            amino_acid = g[1]
            codon_to_amino_acid_dict[codon] = amino_acid

    # Translate using dictionary
    aminos = ""
    for i in range(0, len(s) - 3, 3):
        cod = s[i: i + 3]
        amino = codon_to_amino_acid_dict[cod]
        if amino != "Stop":
            aminos += amino
    return aminos

print prot2(rna_str)

