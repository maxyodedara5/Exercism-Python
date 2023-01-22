"""Counts the words in sentence and thier frequency"""

def count_words(sentence):
    """Counts the words in sentence and thier frequency"""
    punctuation_letters = [".", "?", ",", "-", "_", "!", ":", ";", "&", "@", "$", "%", "^"]
    for punc in punctuation_letters:
        if punc in sentence:
            sentence = sentence.replace(punc," ")

    words = sentence.split()

    # Handling the ' in front and end of words
    for index, _ in enumerate(words):
        while words[index].startswith("'"):
            words[index] = words[index][1:]
        while words[index].endswith("'"):
            words[index] = words[index][:-1]

    # Removing empty characters from words
    while "" in words:
        words.pop(words.index(""))
    words_map = {}

    # Word map generation
    for word in words:
        if word.lower() in words_map:
            words_map[word.lower()] += 1
            continue
        words_map[word.lower()] = 1

    # Removing punctuation leftovers from dictionary
    for punc in punctuation_letters:
        if punc in words_map:
            words_map.pop(punc)
    return words_map
