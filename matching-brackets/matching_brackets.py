"""Check if brackets are present"""

def is_paired(input_string):
    """Check if brackets are present"""
    clean_str = ""
    for character in input_string:
        if character in ["{","}","(",")","[","]"]:
            clean_str += character

    input_string = clean_str
    if len(input_string) % 2 != 0:
        return False

    found = True
    while found:
        if "[]" in input_string:
            input_string = input_string.replace("[]", "")

        if "()" in input_string:
            input_string = input_string.replace("()", "")

        if "{}" in input_string:
            input_string = input_string.replace("{}", "")

        found = bool("[]" in input_string or "()" in input_string or "{}" in input_string)

    if len(input_string) != 0:
        return False
    return True
        