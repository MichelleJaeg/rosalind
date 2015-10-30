import sys
data = sys.stdin.read().split()
months = int(data[0])
litter_size = int(data[1])


def rabbit_pairs(n, k):
    """
    This is a Fibonacci Sequence problem, with the addition of the variable k (see below)

    Begin with one pair of newborn rabbits.
    Rabbits reach reproductive age after one month
    Each pair of reproductive age produces a litter of k pairs every month

    Returns the number of rabbit pairs that will be present after n months
    """
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, (a * k) + b
    return a


print(rabbit_pairs(months, litter_size))
