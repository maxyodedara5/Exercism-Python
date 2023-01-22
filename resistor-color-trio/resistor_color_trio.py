"""Script for resistor color mapping"""

COLOR_MAP = {
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



def label(colors):
    """Resistor color mapping"""
    valu_str = ""
    for col in colors:
        if col.lower() in COLOR_MAP:
            valu_str += str(COLOR_MAP[col.lower()])

    valu_in_ohms = int(valu_str[0:2])
    if int(valu_str[2]) > 0:
        valu_in_ohms = str(valu_in_ohms)
        valu_in_ohms += '0' * int(valu_str[2])
        valu_in_ohms = int(valu_in_ohms)

    if valu_in_ohms % 1000 == 0:
        valu_in_ohms = valu_in_ohms // 1000
        valu_in_ohms = str(valu_in_ohms)
        valu_in_ohms += " kiloohms"
    else:
        valu_in_ohms = str(valu_in_ohms)
        valu_in_ohms += " ohms"

    return valu_in_ohms
