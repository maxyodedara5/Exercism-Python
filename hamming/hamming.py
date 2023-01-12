"""Script for calculating the hamming distance between 2 strings"""

def distance(strand_a, strand_b):
    """Calculates the hamming distance between 2 strings"""
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    hamming_distance = 0
    for index,_ in enumerate(strand_a):
        if strand_a[index] != strand_b[index]:
            hamming_distance += 1

    return hamming_distance
