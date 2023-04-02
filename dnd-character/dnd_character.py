"""DND Character generation"""

import random

def modifier(num):
    """Modifier for consitution"""
    return (num - 10) // 2

class Character:
    """DND Character generation class"""
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        """Ability rolls"""
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        d3 = random.randint(1,6)
        d4 = random.randint(1,6)
        rolls = [d1, d2, d3, d4]
        rolls.sort(reverse = True)
        rolls = rolls[:-1]
        return sum(rolls)
