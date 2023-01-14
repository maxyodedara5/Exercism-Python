"""Check if words and candidates are valid anagrams"""

def find_anagrams(word, candidates):
    """Check if words and candidates are valid anagrams"""
    valid_anagrams = []
    dict_word = {}
    for letter in word.lower():
        if letter in dict_word:
            dict_word[letter] += 1
        else:
            dict_word[letter] = 1

    for candidate in candidates:
        candidate_dict = {}
        for letter in candidate.lower():
            if letter in candidate_dict:
                candidate_dict[letter] += 1
            else:
                candidate_dict[letter] = 1
        if candidate_dict == dict_word and candidate.lower() != word.lower():
            valid_anagrams.append(candidate)

    return valid_anagrams
