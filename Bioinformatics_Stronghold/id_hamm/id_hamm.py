import sys
data = sys.stdin.read().split()
string_1 = data[0]
string_2 = data[1]


def hamming_distance(first_string, second_string):
    """ Takes two equal length strings and returns their hamming distance (the number of mismatched nucleotides). """
    distance = 0
    for i in range(0, len(first_string)):
        if first_string[i] != second_string[i]:
            distance += 1
    return distance


print hamming_distance(string_1, string_2)
