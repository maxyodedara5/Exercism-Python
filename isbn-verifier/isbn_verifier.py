"""Script for verification of ISBN"""

import copy

def is_valid(isbn):
    """Function for verification of ISBN"""
    if "-" in isbn:
        isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    check_other = copy.copy(isbn)
    if "X" in check_other:
        check_other = check_other.replace("X","10")
        if not isbn.endswith("X"):
            return False
    if not check_other.isnumeric():
        return False

    sum_of_nums = 0
    for index,num in enumerate(isbn):
        if num == "X":
            num = 10
        sum_of_nums += int(num) * (10 - index)

    if sum_of_nums % 11 == 0:
        return True
    return False
