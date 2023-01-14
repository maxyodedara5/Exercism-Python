"""Script for Sum of Multiples problem"""

def sum_of_multiples(limit, multiples):
    """Sum of multiples function"""
    sum_of_muls = 0
    for num in range(1,limit):
        for multi in multiples:
            if multi != 0 and num % multi == 0:
                sum_of_muls += num
                break
    return sum_of_muls
