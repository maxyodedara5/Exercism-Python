"""
Script check if the year is leap year
"""

def leap_year(year):
    "Check if a year is leap year"

    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True

        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False
