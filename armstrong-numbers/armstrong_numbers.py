"""Script to check if number provided is armstrong number"""

def is_armstrong_number(number):
    """Check if number provided is armstrong number"""
    number = str(number)
    total_calc_arm = 0
    for digit in number:
        total_calc_arm += int(digit) ** len(number)

    if total_calc_arm == int(number):
        return True
    return False
