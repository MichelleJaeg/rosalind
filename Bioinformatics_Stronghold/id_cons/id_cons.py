import sys
dataset = sys.stdin.read().split(">")
dataset = dataset[1:]

dna_strings = []
for d in dataset:
    dna_list = d.split()[1:]
    dna = "".join(dna_list)
    dna_strings.append(dna)


def consensus(dna_strs):
    """ Takes a collection of equal length DNA strings in FASTA format. Returns a consensus string and profile matrix."""

    the_consensus = []

    profile_a = []
    profile_c = []
    profile_g = []
    profile_t = []
    profiles = []

    for i in range(len(dna_strs[0])):
        counts = {"A": 0, "C": 0, "G": 0, "T": 0}
        consensus_column = []
        profile_column = []
        for string in dna_strs:
            consensus_column.append(string[i])
            profile_column.append(string[i])

        counts["A"] = consensus_column.count("A")
        counts["C"] = consensus_column.count("C")
        counts["G"] = consensus_column.count("G")
        counts["T"] = consensus_column.count("T")
        the_consensus.append(max(counts, key=counts.get))

        profile_a.append(str(profile_column.count("A")))
        profile_c.append(str(profile_column.count("C")))
        profile_g.append(str(profile_column.count("G")))
        profile_t.append(str(profile_column.count("T")))

    the_consensus = "".join(the_consensus)

    profiles.append(profile_a)
    profiles.append(profile_c)
    profiles.append(profile_g)
    profiles.append(profile_t)

    return the_consensus, profiles


consensus_string, the_profile = consensus(dna_strings)
print consensus_string
print "A:", " ".join(the_profile[0])
print "C:", " ".join(the_profile[1])
print "G:", " ".join(the_profile[2])
print "T:", " ".join(the_profile[3])





