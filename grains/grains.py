"""Scripts for grains problem"""

def square(number):
    """Value of grains in square"""
    if not 1<= number <=64:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number - 1)


def total():
    """Sum of all grains in chessboard"""
    all_squares_list = []
    all_squares_list.extend(range(1,65))
    all_squares_list = [2 ** (number - 1) for number in all_squares_list]
    return sum(all_squares_list)
