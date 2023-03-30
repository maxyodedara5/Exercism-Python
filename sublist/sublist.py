"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one, list_two):
    """Checks different sublist and superlist"""
    if len(list_one) == 0 or len(list_two) == 0:
        if len(list_one) == len(list_two):
            return EQUAL

        if len(list_one) == 0:
            return SUBLIST

        if len(list_two) == 0:
            return SUPERLIST

    if len(list_one) == len(list_two):
        for i, _ in enumerate(list_one):
            if list_one[i] != list_two[i]:
                return UNEQUAL
        return EQUAL

    if len(list_one) > len(list_two):
        list_one_str = "".join([str(x) + "," for x in list_one])
        list_two_str = "".join([str(x) + "," for x in list_two])
        if list_two_str in list_one_str:
            return SUPERLIST

    if len(list_one) < len(list_two):
        list_one_str = "".join([str(x) for x in list_one])
        list_two_str = "".join([str(x) for x in list_two])
        if list_one_str in list_two_str:
            return SUBLIST

    return UNEQUAL
