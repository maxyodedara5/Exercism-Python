"""Solution for the problem 6 of Euler"""

def square_of_sum(number):
    """Returns square of sum of nums"""
    number += 1
    sq_of_sum = []
    sq_of_sum.extend(range(number))
    sq_of_sum_total = sum(sq_of_sum) ** 2
    return sq_of_sum_total

def sum_of_squares(number):
    """Returns sum of square of nums"""
    number += 1
    su_of_sq = []
    su_of_sq.extend(range(number))
    sum_total = 0
    for i in range(number):
        sum_total += i ** 2
    return sum_total

def difference_of_squares(number):
    """Returns the difference"""
    diff = square_of_sum(number) - sum_of_squares(number)
    return diff

