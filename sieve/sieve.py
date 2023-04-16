"""Implements Sieve of Eratosthenes"""

def primes(limit):
    """Implements Sieve of Eratosthenes"""
    current_seive = 2

    if limit <=2:
        if limit <= 1:
            return []
        return [2]
    limit = list(range(2, limit + 1))
    while current_seive < limit[-1]:
        current_mul = 2
        multiplier = 1
        while multiplier < limit[-1]:
            multiplier = current_mul * current_seive
            if multiplier in limit:
                limit.remove(multiplier)
            current_mul += 1

        current_seive += 1

    return limit

