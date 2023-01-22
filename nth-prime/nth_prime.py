"""Calculates the nth prime number"""

from functools import cache
import math

def prime(number):
    """Prime number generation for nth"""
    if number < 1:
        raise ValueError('there is no zeroth prime')

    primes = []
    current_num = 2
    while len(primes) != number:
        if is_prime(current_num):
            primes.append(current_num)
        current_num += 1

    return primes[-1]

@cache
def is_prime(number):
    "Checks if number is prime"
    max_div = math.floor(math.sqrt(number))
    for i in range(2, 1 + max_div):
        if number % i == 0:
            return False
    return True
