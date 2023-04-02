"Does encoding decoding and creates a random key for substitution cipher if not key is provided"

import random

LETTER_KEY = {}
KEY_LETTER = {}
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
for num, ltr in enumerate(ALPHABETS):
    LETTER_KEY[ltr] = num
    KEY_LETTER[num] = ltr

class Cipher:
    """Does encoding decoding and creates a random key for
    substitution cipher if not key is provided"""
    def __init__(self, key=None):

        if key is not None:
            self.key = key
        else:
            self.key = ""
            for _ in range(10):
                self.key += random.choice(ALPHABETS.lower())

    def encode(self, text):
        """Encodes the given text"""
        encoded_string = ""
        for index, letter in enumerate(text):
            #print(index,letter, index % len(self.key))
            value_of_letter = LETTER_KEY[letter]
            value_of_key = LETTER_KEY[self.key[index % len(self.key)]]
            new_value = (value_of_key + value_of_letter) % 26
            new_letter = KEY_LETTER[new_value]
            encoded_string += new_letter

        return encoded_string

    def decode(self, text):
        """Decodes the given text"""
        decoded_str = ""
        for index, letter in enumerate(text):
            #print(index,letter, index % len(self.key))
            value_of_letter = LETTER_KEY[letter]
            value_of_key = LETTER_KEY[self.key[index % len(self.key)]]
            new_value = abs((value_of_letter - value_of_key) % 26)
            new_letter = KEY_LETTER[new_value]
            decoded_str += new_letter
        return decoded_str
