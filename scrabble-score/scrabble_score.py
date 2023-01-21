def score(word):
    score_of_word = 0
    for letter in word:
        if letter.upper() in ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]:
            score_of_word += 1
        if letter.upper() in ["D", "G"]:
            score_of_word += 2
        if letter.upper() in ["B", "C", "M", "P"]:
            score_of_word += 3
        if letter.upper() in ["F", "H", "V", "W", "Y"]:
            score_of_word += 4
        if letter.upper() == "K":
            score_of_word += 5
        if letter.upper() in ["J", "X"]:
            score_of_word += 8
        if letter.upper() in ["Q", "Z"]:
            score_of_word += 10
    
    return score_of_word
