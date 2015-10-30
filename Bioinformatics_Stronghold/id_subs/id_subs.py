import sys
dataset = sys.stdin.read().split()
s = dataset[0]
t = dataset[1]


def subs(s, t):
    """ Takes two DNA strings s and t, returns all locations of t as a substring of s. """
    indices = []
    for i in range(0, len(s) - len(t) + 1):
        substring = s[i: i + len(t)]
        if substring == t:
            indices.append(str(i + 1))
    return indices

answer = subs(s, t)
print " ".join(answer)


