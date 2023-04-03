"""Recite poem about bottles"""
NUMBER = {
    10 : "ten",
    9 : "nine",
    8 : "eight",
    7 : "seven",
    6 : "six",
    5 : "five",
    4 : "four",
    3 : "three",
    2 : "two",
    1 : "one",
    0 : "no"
}


def recite(start, take=1):
    """Recite poem about bottles"""
    main_verse = ["NumberCap green bottles hanging on the wall,",
                  "NumberCap green bottles hanging on the wall,", 
                  "And if one green bottle should accidentally fall,", 
                  "There'll be NumberLess green bottles hanging on the wall.",
                  ""]
    main_verse = ":".join(main_verse)
    output_string = []
    for _ in range(take):
        current_string = main_verse.replace("NumberCap", NUMBER[start].capitalize())
        current_string = current_string.replace("NumberLess", NUMBER[start - 1])
        current_string = current_string.split(":")

        for num, i in enumerate(current_string):
            if (("One" in i) or ("one" in i)) and "accidentally" not in i:
                current_string[num] = current_string[num].replace("bottles", "bottle")

        output_string += current_string
        start -= 1

    return output_string[:-1]
