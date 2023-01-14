"""Cartesian geometry to find out score of darts"""

def score(x_co, y_co):
    """Cartesian geometry to find out score of darts"""
    sum_of_sq_co = x_co ** 2 + y_co ** 2


    if 25 < sum_of_sq_co <= 100:
        return 1

    if 1 < sum_of_sq_co <= 25:
        return 5

    if sum_of_sq_co <= 1:
        return 10

    return 0
