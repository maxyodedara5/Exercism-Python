"""Checks allergies more of a lesson in using classes"""

ALLERGENS = {
    "eggs" : 0,
    "peanuts" : 1,
    "shellfish" : 2,
    "strawberries" : 3,
    "tomatoes" : 4,
    "chocolate" : 5,
    "pollen" : 6,
    "cats" : 7
}


class Allergies:
    """Checks allergies"""
    def __init__(self, score):
        self.binary_repr = str(bin(int(score))).replace("0b","")
        if len(self.binary_repr) < len(ALLERGENS):
            self.binary_repr =  "0" * (len(ALLERGENS) - len(self.binary_repr)) + self.binary_repr
        self.binary_repr = self.binary_repr[::-1]
        self.allergens_list = []


    def allergic_to(self, item):
        """Checks for a single item"""
        if self.binary_repr[ALLERGENS[item]] == "1":
            return True
        return False

    @property
    def lst(self):
        """Creates a list of items allergic to"""
        for item, val in ALLERGENS.items():
            if self.binary_repr[val] == "1":
                self.allergens_list.append(item)
        return self.allergens_list
