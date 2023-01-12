"""Script to check if the string provided is pangram"""

def is_pangram(sentence):
    """Function to check if sentence is pangram"""
    sentence = sentence.lower()
    sentence = set(sentence)
    all_alphabets = "abcdefghijklmnopqrstuvwxyz"
    all_alphabets = set(all_alphabets)
    return all_alphabets.issubset(sentence)
