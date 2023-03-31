"""Creates the diamond of the letters"""

def rows(letter):
    """Creates the diamond of the letters"""
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final_string = alphabets[:alphabets.index(letter) + 1]
    final_string = final_string[::-1] + final_string
    final_string = final_string.replace("AA","A")

    diamond = []
    half_range = len(final_string)// 2
    base_letters = alphabets[:alphabets.index(letter) + 1]
    for num in range(0, half_range + 1):
        to_append = ""
        for letter in final_string:
            if letter != base_letters[num]:
                to_append += " "
            else:
                to_append += base_letters[num]
        diamond.append(to_append)

    diamond = diamond + diamond[:half_range][::-1]
    return diamond
