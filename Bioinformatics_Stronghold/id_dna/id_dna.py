import sys
data = sys.stdin.read()


def count_nucleotides(seq):
    """Prints four integers counting the number of times that each nucleotide occurs in the string"""
    a = seq.count("A")
    c = seq.count("C")
    g = seq.count("G")
    t = seq.count("T")
    print a, c, g, t

count_nucleotides(data)
