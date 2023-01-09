"""
Checks if trainge is valid and what type of traingle is it
"""

def equilateral(sides):
    """Check if traingle is equilateral"""

    if not check_if_traingle(sides):
        return False

    if sides[0] == sides[1] == sides[2]:
        return True
    return False


def isosceles(sides):
    """Check if traingle is equilateral"""

    if not check_if_traingle(sides):
        return False
    sides.sort()
    if sides[0] == sides[1] or sides[1] == sides[2]:
        return True
    return False


def scalene(sides):
    """Check if traingle is equilateral"""

    if not check_if_traingle(sides):
        return False
    if sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]:
        return True
    return False


def check_if_traingle(sides):
    """Check if traingle has valid sides"""
    for side in sides:
        if side == 0:
            return False

    if sides[0] + sides[1] < sides[2]:
        return False

    if sides[1] + sides[2] < sides[0]:
        return False

    if sides[0] + sides[2] < sides[1]:
        return False

    return True
