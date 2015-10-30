import sys
dataset = sys.stdin.read().split(">")
dataset = dataset[1:]


def gc(data):
    """ Takes 10 DNA strings in FASTA format, returns the ID and GC-content of the one with the highest GC-content. """
    highest_gc = 0
    highest_gc_id = ""
    for d in data:
        ros_id = d.split()[0]
        dna_list = d.split()[1:]
        dna = "".join(dna_list)
        # Calculate percentage of nucleotides that are G or C in the DNA string
        gc_count = 0
        total_nuc_count = 0
        for nuc in dna:
            if nuc == "C" or nuc == "G":
                gc_count += 1
            total_nuc_count += 1
        gc_perc = gc_count / float(total_nuc_count)
        # Find out if gc percentage is highest so far
        if gc_perc > highest_gc:
            highest_gc = gc_perc
            highest_gc_id = ros_id
    return (highest_gc_id, highest_gc * 100)


output = gc(dataset)
for value in output:
    print value



