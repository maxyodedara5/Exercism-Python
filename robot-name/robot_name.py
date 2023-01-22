"""Robots name generation"""

import random

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"

class Robot:
    """Robot name generation"""
    def __init__(self):
        self.name = self.generate_name()

    def reset(self):
        """Resets the name of robot"""
        while self.generate_name() == self.name:
            self.name = self.generate_name()

    @staticmethod
    def generate_name():
        """Static method for generation of robot name"""
        rand_letters = random.choices(LETTERS, k=2)
        rand_nums = random.choices(NUMBERS, k=3)
        return "".join(rand_letters) + "".join(rand_nums)
