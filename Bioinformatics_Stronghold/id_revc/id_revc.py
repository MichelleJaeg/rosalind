import sys
data = sys.stdin.read()
from string import maketrans


def reverse_complement(seq):
    """Returns the reverse complement of a DNA string."""

    # Translate original string to complements
    in_str = "ACGT"
    out_str = "TGCA"
    from_to = maketrans(in_str, out_str)
    complements = seq.translate(from_to)

    # Return reverse string
    return complements[::-1]


print reverse_complement(data)
