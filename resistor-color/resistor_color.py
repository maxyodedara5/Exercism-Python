"""RESISTANCE COLOUR MAPPINGS"""

color_dict = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

def color_code(color):
    """Gives color value as per code"""
    return color_dict[color]

def colors():
    """Colors from the dict"""
    return list(color_dict.keys())
