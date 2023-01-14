"""Script for converting the sound of number"""

def convert(number):
    """Script for converting the sound of number"""
    number = int(number)
    sound = ""
    if number % 3 == 0:
        sound += "Pling"

    if number % 5 == 0:
        sound += "Plang"

    if number % 7 == 0:
        sound += "Plong"

    if number % 3 != 0 and number % 7 != 0 and number % 5 != 0:
        sound = str(number)

    return sound
