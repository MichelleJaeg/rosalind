import sys
data = sys.stdin.read()


def dna_to_rna(seq):
    """Returns the original string with T replaced by U."""
    return seq.replace("T", "U")


print dna_to_rna(data)
