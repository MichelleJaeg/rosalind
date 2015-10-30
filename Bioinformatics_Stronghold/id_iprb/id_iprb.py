import sys
import random
data = sys.stdin.read().split()
k_num = int(data[0])
m_num = int(data[1])
n_num = int(data[2])


def iprb(k, m, n):
    """

    Takes three positive integers representing a population containing k + m + n organisms. k individuals are
    homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

    Returns the probability that two randomly selected mating organisms will produce an individual possessing a dominant
    allele.

    This function uses simulation to find the solution.

    """

    # Randomly choose two organisms from the population
    population = []
    for i in range(k):
        population.append("k")
    for j in range(m):
        population.append("m")
    for t in range(n):
        population.append("n")

    organism_1 = random.choice(population)

    # Remove organism that was chosen already from population pool
    population.remove(organism_1)

    organism_2 = random.choice(population)

    # One or Two homozygous dominant organisms return a dominant allele for that factor
    if organism_1 == "k" or organism_2 == "k":
        return "dominant"
    # Two homozygous recessive organisms return a recessive allele for that factor
    elif organism_1 == "n" and organism_2 == "n":
        return "recessive"
    # Two heterozygous organisms return a dominant allele at .75 probability or a recessive allele at .25 probability
    elif organism_1 == "m" and organism_2 == "m":
        x = random.random()
        if x <= .75:
            return "dominant"
        else:
            return "recessive"
    # All other combinations are 50/50 for dominant or recessive
    else:
        y = random.random()
        if y <= .5:
            return "dominant"
        else:
            return "recessive"


def simulation(n):
    dominant_count = 0
    total_count = 0

    for i in range(n):
        result = iprb(k_num, m_num, n_num)
        if result == "dominant":
            dominant_count += 1
        total_count += 1

    return dominant_count / float(total_count)

print(simulation(100000))

