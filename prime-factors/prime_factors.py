"""Finds out prime factors"""

def factors(num):
    """Finds out prime factors"""
    start_prime = 2
    prime_factors = []
    while num > 1:
        if num % start_prime == 0:
            prime_factors.append(start_prime)
            num = num // start_prime
        else:
            start_prime += 1
    return prime_factors
